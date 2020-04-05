import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='node_user', password='1111',
                       db='node_schema', charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
# SQL문 실행
sql = "select * from customers"
curs.execute(sql)
 
# 데이타 Fetch
rows = curs.fetchall()

for row in rows:
    print(row)
 
# Connection 닫기
conn.close()