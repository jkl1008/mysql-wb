import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="test_db"
    )
 
mycursor = mydb.cursor()

sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"
mycursor.execute(sql)
mydb.commit()


print(mycursor.rowcount, " 条记录被修改")
