# # -*- coding: utf-8 -*-
# # @Time    : 2021/4/27 11:55
# # @Author  : SunnyTang
# # @Site    : python3批量向Mysql中插入数据
# # @File    : test_mysql.py
# import pymysql
# import random
#
# # 数据库连接
# db = pymysql.connect(host='xx.xxx.xxx.xx', port=xxxx,
#                      user='xx', passwd='xx', db='', charset='utf8')
# cursor = db.cursor()
# data = list()
#
#
# # 生成随机手机号码
# moblie = []
# for i in range(2):
#     prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
#                "153", "155", "156", "157", "158", "159", "186", "187", "188"]
#     shoujihao = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
#     moblie.append(shoujihao)
#
# # 随机生成id
#
# list_id = []
#
# for i in range(2):
#     id = random.sample("1234567890732749274823742",19)  # 用户名长度通过更改后面数字变化
#     # print(''.join(name))
#     list_id.append(''.join(id))
# print(list_id)
#
# # 随机生成username
#
# list_username = []
# for i in range(2):
#     username = random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*",8)  # 用户名长度通过更改后面数字变化
#     # print(''.join(name))
#     list_username.append(''.join(username))
# print(list_username)
#
# # 随机生成用户名
# list = []
# for i in range(2):
#     name = random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*",8)  # 用户名长度通过更改后面数字变化
#     # print(''.join(name))
#     list.append(''.join(name))
# print(list)
#
# # 多条随机数据插入数据库
# for i in range(2):
#     password = ["100", "100", "100"]
#     value = (list_id[i],random.choice(password),list_username[i],list[i],moblie[i])
#     data.append(value)
#
#
# # 插入数据库方法及指令
# def insert_data():
#     sql = "INSERT INTO member(id,type,user_name,name,mobile) VALUES (%s,%s,%s,%s,%s)"
#     try:
#         cursor.executemany(sql, data)
#         db.commit()
#         print("insert success")
#     except:
#         db.rollback()
#
#
# #if __name__ == '__main__':
# #   insert_data()