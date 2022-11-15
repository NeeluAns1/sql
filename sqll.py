import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin2',
                   database='neelu',
                     cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s" % data)
