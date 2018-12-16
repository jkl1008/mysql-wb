import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="test_db"
    )
 
mycursor = mydb.cursor()

sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"
sql = "INSERT INTO sites (name, url) VALUES ("RUNOOB", "https://www.runoob.com")" # 插入数据
sql =  "CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))" # 主键设置
sql = "SELECT * FROM sites WHERE name ='RUNOOB'" # 条件查询
sql = "SELECT * FROM sites ORDER BY name"# 排序查询
sql = "DELETE FROM sites WHERE name = 'stackoverflow'" # 删除记录
sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'" # 更新数据
sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites 


mycursor.execute(sql)
mydb.commit()


print(mycursor.rowcount, " 条记录被修改")
