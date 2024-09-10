import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='alki',
    database='telecom'
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()
        print("Database version:", result)
finally:
    connection.close()
