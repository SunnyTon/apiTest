# # -*- coding: utf-8 -*-
# # @Time    : 2021/6/11 15:25
# # @Author  : SunnyTang
# # @FileName: examda_activity_data.py
# import pymysql
# import random
#
# # 数据库连接
# db = pymysql.connect(host='xx.xxx.xxx.xx', port=xxxx,
#                      user='xx', passwd='xx', db='', charset='utf8')
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 使用execute方法执行SQL语句
# cursor.execute("select eap.PrizeName,count(*) from  Examda_Activity AS ea
# LEFT JOIN Examda_Activity_Prize AS eap ON eap.Id=ea.PrizeId
# where ActivityType = 59 and DetailId = 848 and PrizeId != 4001
# GROUP BY ea.PrizeId,eap.prizename")
#
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
#
# print "Database version : %s " % data
#
# # 关闭数据库连接
# db.close()
#
#
# #if __name__ == '__main__':
# #   insert_data()