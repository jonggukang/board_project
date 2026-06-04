import pymysql

class BoardDAO:
    def __init__(self):
        self.host = "localhost" # 127.0.0.1
        # self.port = 3306 # 위 컴퓨터에서 mysql을 찾는 방식. default: 3306 (오라클은 8080)
        self.user = "board_user"
        self.password = "board1234"
        self.database = "board_db"

    def get_connection(self):
        return pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
            charset = "utf8mb4" # 이모지까지 포함한 utf8
        )
    
    def select_all(self):
        conn = self.get_connection() # 통로가 생기고
        cursor = conn.cursor() # 연결된 connection에 sql문 실행할 때 파이썬에서 제공하는 데이터 타입으로 리턴

        sql = "select * from Board order by id DESC"

        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close() # close(): 안에 있는 것부터 닫아야 함
        conn.close()

        return result