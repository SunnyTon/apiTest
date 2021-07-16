# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 16:27
# @Author  : SunnyTang
# @FileName: index.py

import json
import pytest
import allure
import requests


@allure.feature('打开首页')  # feature定义功能
class TestShoppingTrolley(object):
    @allure.story('加入购物车')  # story定义用户场景
    def test_add_shopping_trolley(self):
        login('刘春明', '密码')  # 调用“步骤函数”
        with allure.step("浏览商品"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤2
            allure.attach('商品1', '刘春明')  # attach可以打印一些附加信息
            allure.attach('商品2', 'liuchunming')
        with allure.step("点击商品"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤3
            pass
        with allure.step("校验结果"):
            allure.attach('期望结果', '添加购物车成功')
            allure.attach('实际结果', '添加购物车失败')
            assert 'success' == 'failed'

    @allure.story('修改购物车')
    def test_edit_shopping_trolley(self):
        pass