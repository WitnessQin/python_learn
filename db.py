#coding=utf-8
import MySQLdb
#import pymysql
#pymysql：pymsql是Python中操作MySQL的模块，其使用方法和MySQLdb几乎相同。但目前pymysql支持python3.x而后者不支持3.x版本

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='test',
        )
cur = conn.cursor()

#创建数据表
cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
#插入一条数据
cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
#修改查询条件的数据
cur.execute("update student set class='3 year 1 class' where name = 'Tom'")
#删除查询条件的数据
cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()