# # -*- coding: utf-8 -*-
# # @Time    : 2021/4/26 16:55
# # @Author  : SunnyTang
# # @FileName: test_pytest.py
#
# import pytest
# import os
#
#
# class Test_Pytest():
#
#     def test_one(self):
#         print("test_one方法执行")
#         assert 1 == 1
#
#     def test_two(self):
#         print("test_two方法执行")
#         assert "s" in "love"
#
#     def test_three(self):
#         print("test_three方法执行")
#         assert 3 - 2 == 1
#
# #
# # if __name__ == "__main__":
# #    pytest.main(['-s', '-q', '--alluredir', 'report/result', 'test_Pytest.py'])