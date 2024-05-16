from sql.databases import PymysqlClass

"""
连接MySQL数据库
"""


def create_db():
    db = PymysqlClass(host='#', user='root', password='#', database='face_card',
                      port=3306)
    db.connect()
    cursor = db.get_cursor()
    print('连接到数据库')
    return db, cursor
