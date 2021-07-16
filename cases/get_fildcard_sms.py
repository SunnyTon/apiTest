# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 11:23
# @Author  : SunnyTang
# @FileName: get_fildcard_sms.py

class TestShoppingTrolley(object):
      """
         实物奖品数量监控脚本，超量短信告警监控
      后台监控地址：
      https://support.233.com/tiku/activity/newwinnerslog?pageIndex=1&pageSize=20&sort=id&order=desc&activityId=848&prizeId=4001
        1、定义获取数据库实物总数
        2、断言获奖实物是否超量？yes：sms发送短信
        3、jenkin跑脚本，1h跑一次，
      """
      IPAD=1
      SKG=1
      ShouHuan=1
      XiaoMi=1
      T_Shirt=1
      Bag=1
      SportsWatch=1
      MAC_KH=1
      BZ=1
      def __test__(self):
         if(self.a!=self.IPAD):
               pass
         else:
               pass
