#!/usr/bin/python3

import pymysql
import random
import os
import string

num1 = random.randint(1000, 9999)
username = "testerkara" + str(num1)
print(username)

num2 = random.randint(70000000, 79999999)
phone = "186" + str(num2)
print(phone)

num3 = random.randint(100000, 999999)
num4 = random.randint(1000, 9999)
identity = str(num4) + "19900101" +str(num4)
print(identity)

# 打开数据库连接
db = pymysql.Connect(host='mysql-cn-south-1-36f43c39281c45a4.public.jcloud.com', port=3306, user='recycling_root', passwd='Recycling2018', db='recycling_testing', charset='UTF8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)




# 向数据库表插入数据
# 下面是value总带有变量的情况
sql = """INSERT INTO EMPLOYEES (NAME, SECRET, ENTRY_TIME, STATE, MOBILE_PHONE, IDENTITY, PASSWORD, SEX, USERNAME, CITY_CODE, COUNTY_CODE, PROVINCE_CODE, STREET_CODE, POST_ID)
      VALUES ('TANXUEQIN', '9cd58d1c-d906-4967-b347-c26af72f3b17', '2018-11-07 10:07:36', 'Normal', '%s', '%s', '$2a$10$.abrEl5oFSB4ImgUXovTKOiVGct4NX1NcNcOwRmqh.tJiiNd1stjW', 'Male', '%s', '350600', '350603', '350000', '350603100', 1)"""%(phone, identity, username)
print(sql)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()




# 查询刚刚插入的记录，并获取id值
# 下面是条件中带有变量的情况
sql = "SELECT* FROM EMPLOYEES WHERE USERNAME='%s'"%(username)

try:
    cursor.execute(sql)
    print(sql)
    result = cursor.fetchone()
    employee_id = result[0]
    print(employee_id)
except:
    print("Error:unable to fatch data")





# 向employee_roles表中插入该员工的role
sql = """INSERT INTO EMPLOYEE_ROLES(EMPLOYEE_ID, ROLE_ID)
      VALUES (%d, 4)"""%(employee_id)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()


# 更新刚刚插入employees表中的记录数据
sql = "UPDATE EMPLOYEES SET SEX = 'Female' WHERE ID = %d"%(employee_id)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()



# 删除刚刚插入的数据  因为employees和employee_roles存在关联  要先删除角色表中数据 再删除成员表中数据
sql = "DELETE FROM EMPLOYEE_ROLES WHERE EMPLOYEE_ID = %d"%(employee_id)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

sql = "DELETE FROM EMPLOYEES WHERE ID = %d"%(employee_id)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()



# 关闭数据库连接
db.close()



