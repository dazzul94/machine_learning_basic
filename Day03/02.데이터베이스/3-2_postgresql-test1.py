import psycopg2
import pandas as pd

user = 'postgres'
password = '1234'
host_product = 'localhost'
dbname = 'dvdrental'
port='5432'

product_connection_string = "dbname={dbname} user={user} host={host} password={password} port={port}"\
                            .format(dbname=dbname,
                                    user=user,
                                    host=host_product,
                                    password=password,
                                    port=port)    
try:
    conn = psycopg2.connect(product_connection_string)
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

#쿼리 입력
query = """
select customer_id from customer
"""

#일반적인 쿼리 조회 방법
cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print("customer_id = {} ".format(row[0]))

#pandas를 통한 조회 방법
pd.read_sql("select customer_id from customer", conn)