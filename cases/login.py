# # -*- coding: utf-8 -*-
# # @Time    : 2021/4/28 8:19
# # @Author  : SunnyTang
# # @FileName: login.py
# # from tools import Basic
# # import Assert
# import json
# import pytest
# import allure
# import requests
#
#
# class TestLogin:
#     @allure.feature('Home')  # feature定义业务接口
#     @allure.severity('blocker')
#     @allure.story('Login')  # story定义接口场景
#     def test_login_01():
#         """
#            用例描述：未登陆状态下查看基础设置
#         """
#         #conf = Config() config还没封装读取配置信息
#         # data = Basic()
#         #test = Assert.Assertions()
#         # request = Request.Request(action)
#
#         # host = conf.host_debug
#         url = "https://japi.233.com/ess-ucs-api/doz/do/login/common" #+host
#         params = {
#             "captchaKey": "rzx9mtymqojlrvr6g0osswsx34vqsdyj",
#             "loginFrom": 1,
#             "loginPlatform": 1,
#             "platFrom": "pc",
#             "redirectUrl": "https%3a%2f%2fwx.233.com%2fuc%2fuser",
#             "url": "http://passport.233.com/login/?redirectURL=https%3a%2f%2fwx.233.com%2fuc%2fuser",
#             "originUrl": "",
#             "originSource": "直接访问",
#             "registChannel": "直接访问",
#             "deviceId": "9df65a74-df4b-4ac3-8fab-8266dcafc35a",
#             "deviceBrand": "Windows 10",
#             "appVersion": "谷歌 Chrome/89.0.4389.90",
#             "username": "15901759418",
#             "password": "513f0b2737862693bd54573b745cde1b",
#             "captcha": ""
#         }
#         headers = {'content-type': "application/json"}
#         response = requests.post(url=url, data=json.dumps(params), headers=headers)
#         # d = json.loads(response.text)
#         assert response.status_code == 200
#
#     @allure.feature('Home2')  # feature定义业务接口
#     @allure.severity('normal')
#     @allure.story('Login2')  # story定义接口场景
#     def test_login_02(self):
#         assert 1 == 1
