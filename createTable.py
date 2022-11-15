import pymysql.cursors
db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin2',
                     database='neelu',
                     cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
query= "create table nm (fname varchar(100), laname varchar(100),age int(10))"
try:
     cursor.execute(query)
     db.commit()
except:
     db.rollback()

db.close()