import pandas as pd
from board_dao import *

board_dao = BoardDAO()
board_dao.get_connection() # 커넥션 테스트

while True:
    try:
        print("=" * 40)
        print("1.목록  2.등록 3.내용 4.삭제 0.종료")
        print("=" * 40)

        menu = input("선택 > ")

        if menu == "0":
            break
        elif menu == "1": # 목록
            boards = board_dao.select_all()

            result = pd.DataFrame(list(boards), index=None) # https://stackoverflow.com/questions/33700626/how-to-convert-tuple-of-tuples-to-pandas-dataframe-in-python
            result = result.iloc[:, [0, 1, 2, 3, 4, 5, 7]]
            result.columns = ['번호', '제목', '내용', '작성자', '등록일시', '수정일시', '추천수']
            result = result.set_index('번호')
            print(result)

            '''
            for board in boards:
                print(str(board[0]) + "\t|\t" + board[1] + "\t|\t" + board[3] + "\t|\t" + str(board[7]) + "\t")
            '''

        elif menu == "2": # 등록
            writer = input("이름 > ")
            title = input("제목 > ")
            content = input("내용 > ")
            pwd = input("비밀번호 > ")

            item = [{'title': title, 'writer': writer, 'content': content, 'password': pwd, 'reaction': 0}]
            board_dao.create_item(item)

        elif menu == "3": # 내용
            request_id = input("글번호 > ")

            result = board_dao.open_item(request_id)
            # print(result)
            result_df = pd.DataFrame(result)
            result_df = result_df.iloc[[0, 1, 2, 3, 4, 5, 7], :]
            result_df.columns = ['글 내용']
            result_df.index = ['글번호', '제목', '내용', '작성자', '등록일시', '수정일시', '추천수']
            print(result_df)

            print("=" * 40)
            print("1.좋아요  2.목록으로")
            print("=" * 40)

            submenu = input("선택 > ")

            if submenu == "1":
                board_dao.add_reaction(request_id)
                # print(board_dao.open_item(request_id))
            elif submenu == "2":
                boards = board_dao.select_all()

                result = pd.DataFrame(list(boards), index=None) # https://stackoverflow.com/questions/33700626/how-to-convert-tuple-of-tuples-to-pandas-dataframe-in-python
                result = result.iloc[:, [0, 1, 2, 3, 4, 5, 7]]
                result.columns = ['번호', '제목', '내용', '작성자', '등록일시', '수정일시', '추천수']
                result = result.set_index('번호')
                print(result)
            else:
                print("유효하지 않은 명령입니다. 처음으로 돌아갑니다.")

        elif menu == "4": # 삭제
            while True:
                request_id = input("글번호 > ")
                request_pw = input("비밀번호 > ")

                result = board_dao.open_item(request_id)
                # print(result)

                if request_pw == result[6]:
                    board_dao.delete_item(request_id)
                    print("게시물이 삭제되었습니다.")
                    break
                else:
                    print("잘못된 비밀번호입니다.")

        elif menu == "0":
            print("프로그램 종료")
            break
        else:
            print("유효하지 않은 명령입니다.")
    except Exception as e:
        print("에러가 발생했습니다:", e)
        break




print("게시판 종료")
