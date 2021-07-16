# # # -*- coding: utf-8 -*-
# # # @Time    : 2021/4/26 16:55
# # # @Author  : SunnyTang
# # # @FileName: test_case.py
# # import allure
# # import pytest
# #
# #
# # test_case_01为用例title
# @allure.feature('test_module_01')
# @allure.story('test_story_01')
# @allure.severity('blocker')
# @allure.step
# def test_case_01():
#     """
#     用例描述：Test case 01
#     """
#     assert "2" == false
#
#
# @allure.feature('test_module_01')
# @allure.story('test_story_02')
# @allure.severity('critical')
# def test_case_02():
#     """
#     用例描述：Test case 02
#     """
#     assert '1' == 1
#
#
# @allure.feature('test_module_01')
# @allure.story('test_story_03')
# @allure.severity('normal')
# def test_case_03():
#     """
#     用例描述：Test case 03
#     """
#     assert 1 == '1'
#
#
# @allure.feature('test_module_01')
# @allure.story('test_story_04')
# @allure.severity('minor')
# def test_case_04():
#     """
#     用例描述：Test case 04
#     """
#     assert 0 == true
#
#
# @allure.feature('test_module_01')
# @allure.story('test_story_05')
# @allure.severity('trivial')
# def test_case_05():
#     """
#     用例描述：Test case 05
#     """
#     assert 0 == 0