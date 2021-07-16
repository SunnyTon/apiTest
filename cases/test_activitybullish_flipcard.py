# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 15:14
# @Author  : SunnyTang
# @FileName: test_activitybullish_flipcard.py


import json
import pytest
import allure
import requests


@allure.feature('618牛气冲天游戏抽卡相关接口')  # feature定义功能
class TestActivityBullishFlipCard(object):
    def getBullishInfo(self,callback,activityId,timestamp):
        """ 用例描述：获取牛气活动信息 缺少cookie """
        headers = {'content-type': "application/json"}
        url = "https://api.233.com/sitenews/api/v1/activitybullish/GetBullishInfo"
        params = {
            "callback": callback,
            "activityId": activityId,
            "_": timestamp
        }
        res = requests.get(url=url, data=json.dumps(params), headers=headers)
        allure.attach(str(headers),"Headers: ")  # 往报告中添加请求头
        allure.attach(str(url),"Url: ") # 往报告中添加请求地址
        allure.attach(str(params),"Params: ") # 往报告中添加请求参数
        allure.attach(str(res.status_code), "Status：")  # 往报告中添加响应状态码
        allure.attach(str(res.text),"Body: ") # 往报告中添加响应结果
        allure.attach("Actual：" + str(res.json()['s']))  # 往报告中添加断言结果
        return res.json()

    @allure.severity('CRITICAL')  # severity定义用例等级
    @allure.story('GetBullishInfo')  # story定义接口场景
    @allure.step('正确的活动Id')# 用例步骤-->后期建议--☆封装成模板☆--
    def test_get_bullish_info_01(self):
        """ 测试获取牛气冲天信息：正确的callback、activityId、timestamp """
        callback = "jQuery21106655809859394386_1622799698917",
        activityId = 848,
        timestamp= 1622799698918,
        result = self.getBullishInfo(callback,activityId,timestamp)
        assert result.json()['s'] == 10006  # 提取响应结果中的s作为断言

    @allure.severity('BLOCKER')  # severity定义用例等级
    @allure.story('GetBullishInfo')  # story定义接口场景
    @allure.step('参数全为空')
    def test_get_bullish_info_02(self):
        """ 测试获取牛气冲天信息：参数为空callback、activityId、timestamp """
        callback = "",
        activityId = "",
        timestamp = "",
        result = self.getBullishInfo(callback, activityId, timestamp)
        assert result.status_code == 200  # 提取响应结果中的s作为断言

    @allure.severity('Normal')  # severity定义用例等级
    @allure.story('GetBullishInfo')  # story定义接口场景
    @allure.step('错误的活动Id')
    def test_get_bullish_info_02(self):
        """ 测试获取牛气冲天信息：参数为空callback、activityId、timestamp """
        callback = "",
        activityId = 0,
        timestamp = "",
        result = self.getBullishInfo(callback, activityId, timestamp)
        assert result.status_code == 200  # 提取响应结果中的s作为断言

    @allure.severity('blocker')  # severity定义用例等级
    @allure.story('AddBullishValue')  # story定义接口场景
    def test_add_bullish_value(self):
        """
           用例描述：累计牛气值
        """
        url = "https://api.233.com/sitenews/api/v1/activitybullish/AddBullishValue"
        params = {
            "callback": "jQuery21106655809859394386_1622799698917",
            "activityId": 848,
            "_": 1622799698918
        }
        headers = {'content-type': "application/json"}
        response = requests.get(url=url, data=json.dumps(params), headers=headers)
        data = response.json()  # 将响应结果转成json对象
        s = data.get('s')  # 提取key对象的value
        with allure.step("正确的参数"):
            allure.attach(str(headers), "Headers: ")  # 往报告中添加请求头
            allure.attach(str(url), "Url: ")  # 往报告中添加请求地址
            allure.attach(str(params), "Params: ")  # 往报告中添加请求参数
            allure.attach(str(response.status_code), "Status：")  # 往报告中添加响应状态码
            allure.attach(str(response.text), "Body: ")  # 往报告中添加响应结果
            allure.attach("Actual：" + str(response.json()['s']), "Expect: " + str(10006))  # 往报告中添加断言结果
        assert s == 10006  # 提取响应结果中的s作为断言
        with allure.step("参数为空"):
            pass
        assert response.status_code == 200

    @allure.severity('blocker')  # severity定义用例等级
    @allure.story('FlipCard')  # story定义接口场景
    def test_flid_card(self):
            """
               用例描述：翻卡
               1、若有次数，正常翻卡
               2、若缺抽卡次数时，数据库自动调用增加次数，再翻卡
            """
            url = "https://api.233.com/sitenews/api/v1/activitybullish/FlipCard"
            params = {
                "callback": "jQuery21106655809859394386_1622799698917",
                "activityId": 848,
                "_": 1622799698918
            }
            headers = {'content-type': "application/json"}
            response = requests.get(url=url, data=json.dumps(params), headers=headers)
            d = json.loads(response.text)
            with allure.step("正确的参数"):
                allure.attach(str(headers), "Headers: ")  # 往报告中添加请求头
                allure.attach(str(url), "Url: ")  # 往报告中添加请求地址
                allure.attach(str(params), "Params: ")  # 往报告中添加请求参数
                allure.attach(str(response.status_code), "Status：")  # 往报告中添加响应状态码
                allure.attach(str(response.text), "Body: ")  # 往报告中添加响应结果
                allure.attach("Actual：" + str(response.json()['s']), "Expect: " + str(10006))  # 往报告中添加断言结果
            assert response.json()['s'] == 10006  # 提取响应结果中的s作为断言
            with allure.step("参数为空"):
                pass
            assert response.status_code == 200