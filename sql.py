from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123123',
)

conn.select_db('student')
cursor = conn.cursor()
cursor.execute('select * from stu')
results: tuple[tuple] = cursor.fetchall()
# print(results)
# cursor.execute('insert into stu values(1, "哈哈哈", 99, "男")')
cursor.execute('update stu set id = 25 where name = "哈哈哈"')
conn.commit()

conn.close()
