import pymysql

conn = pymysql.connect(
    user='root',
    passwd='1111',
    host='localhost',
    db='test'
)

cur = conn.cursor()

cur.execute('drop table if exists items')
cur.execute(''' 
    create table items(
        item_id integer primary key auto_increment,
        name text,
        price integer
    )
''')
data = [('banana', 300), ('mango', 600), ('apple', 200)]
for i in data: 
    cur.execute('insert into items(name, price) values (%s, %s)', i)

cur.execute('select * from items')
for row in cur.fetchall():
    print(row)
# 커밋!!
conn.commit()

# Connection 닫기
conn.close()
