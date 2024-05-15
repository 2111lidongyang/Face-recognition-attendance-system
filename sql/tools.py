from sql.databases import PymysqlClass

"""
连接MySQL数据库
"""


def create_db():
    db = PymysqlClass(host='43.143.229.40', user='root', password='team2111..', database='face_card',
                      port=3306)
    db.connect()
    cursor = db.get_cursor()
    print('连接到数据库')
    return db, cursor
