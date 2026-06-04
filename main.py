from board_dao import *

board_dao = BoardDAO()
board_dao.get_connection() # 커넥션 테스트

while True:
    print("=" * 40)
    print("1.목록  2.등록 3.내용 4.삭제 0.종료")
    print("=" * 40)

    menu = input("선택 > ")

    if menu == "0":
        break
    elif menu == "1": # 목록
        boards = board_dao.select_all()
        # print(boards) # tuple로 출력

        for board in boards:
            print(board[0], board[1], board[2], board[3])


print("게시판 종료")

# 과제: CRUD 만들어서 완성