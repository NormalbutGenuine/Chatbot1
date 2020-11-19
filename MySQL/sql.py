import pymysql
db = None
try:
    db = pymysql.connect(
        host='127.0.0.1',
        user = 'root',
        passwd = 'tiger',
        db='chatbot',
        charset='utf8'
    )
    print("DB연결성공")
except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
        print("DB 연결 닫기 성공")
