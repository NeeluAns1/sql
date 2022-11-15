import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin2',
                     database='neelu',
                     cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
query='INSERT INTO student VALUES("NITY","Dell",23,45787654)'

try:
           cursor.execute(query)
           db.commit()
except:
            db.rollback()
db.close()
