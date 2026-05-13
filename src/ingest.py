import os 
import psycopg2

# 1. Grab credentials from the environment
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT', 5432)

conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_pass,
    host=db_host,
    port=db_port
)

cur = conn.cursor()

sql = """
CREATE TABLE hospitals
(
id integer,
name text
)
"""

cur.execute(sql)
conn.commit()
cur.close()
conn.close()
