import pymysql

conn = pymysql.connect(
    user='root',
    passwd='1111',
    host='localhost',
    db='test'
)

cur = conn.cursor()

cur.execute('select version()')
data = cur.fetchone()
print("Database version : %s " % data)

# Connection 닫기
conn.close()
