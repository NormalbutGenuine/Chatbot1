import pymysql
import openpyxl

from chatbot.config.DatabaseConfig import *

def all_clear_train_data(db):
    sql = '''
        delete from chatbot_train_data
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)

    sql='''
        ALTER TABLE chatbot_train_data AUTO_INCREMENT=1
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)

def insert_data(db, xls_row):
    intent, ner, query, answer, answer_img_url = xls_row

    sql = '''
        INSERT chatbot_train_data(intent, ner, query, answer, answer_image)
        values(
            '%s', '%s', '%s', '%s', '%s'
        )
    ''' % (intent.value, ner.value, query.value, answer.value, answer_img_url.value)

    #엑셀에서 불러온 셀에 데이터가 없는 경우 널로 반환
    sql = sql.replace("'None'", "null")
    with db.cursor() as cursor:
        cursor.execute(sql)
        print('{} 저장'.format(query.value))
        db.commit()

train_file = 'C:\\Users\\obybk\\OneDrive\\바탕 화면\\인공지능\\deepChat\\chatbot\\train_tools\\qna\\train_data.xlsx'
db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user = DB_USER,
        passwd=DB_PASSWORD,
        db = DB_NAME,
        charset = 'utf8'
    )
    #초기화
    all_clear_train_data(db)
    # 학습 엑셀 파일 불러오기

    wb = openpyxl.load_workbook(train_file)
    sheet = wb['Sheet1']
    for row in sheet.iter_rows(min_row=2):
        insert_data(db, row)

    wb.close()
    print("성공")
except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()