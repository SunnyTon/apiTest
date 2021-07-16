# # -*- coding: utf-8 -*-
# # @Time    : 2021/4/27 11:55
# # @Author  : SunnyTang
# # @FileName: senddingtalk.py
# import unittest
# import time from BSTestRunner
# import BSTestRunner from selenium
# import webdriver from selenium.webdriver.chrome.options#定义chrome无头浏览器
# import Options from dingtalkchatbot.chatbot
# import DingtalkChatbot    #发送通知到钉钉机器人
# # 指定测试用例和测试报告的路径
# test_case_dir = './XXX_test_case'
# test_reports_dir = './XXX_test_reports'# 定义测试报告文件格式
# now = time.strftime('%Y-%m-%d %H_%M_%S')
# test_report_name = test_reports_dir+'/'+now+' XXX_test_resport.html'
# # 加载测试用例print('开始执行测试用例')
# discover = unittest.defaultTestLoader.discover(test_case_dir,pattern='XXX_test.py')
# # 运行测试用例并生成测试报告
# print('开始生成测试报告...')
# with open(test_report_name,'wb') as f:
#     runner = BSTestRunner(stream=f,title='XXX接口自动化测试报告',description='这是关于XXX的接口自动化测试报告')
#     runner.run(discover)
#     f.close()
# # 获取测试报告
# urltest_reports_url = 'file:///your_object_path'+test_report_name
# # 用你的实际项目根目录替换
# #your_object_pathprint('测试报告的地址是：{}'.format(test_reports_url))
# # chrome无头浏览器,打开测试报告
# urlchrome_options = Options()
# chrome_options.add_argument('- -headless')
# chrome_options.add_argument('- -disable-gpu')
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get(test_reports_url)
# time.sleep(5)
# print('测试报告的名称是：{}'.format(driver.title))# 检测报告内容是否有用例fail，有则发送通知到钉钉机器人element = driver.find_element_by_xpath('//*[@id="result_table"]/tbody/tr[1]/td[4]')
# fail_text = element.get_attribute('textContent')
# print('报错用例数量有： {} 个'.format(fail_text))if fail_text != '0':    # 发送通知到钉钉机器人
#     print ('报告已生成，但有异常用例，开始发送通知到钉钉机器人...' )
#     webhook = 'https://oapi.dingtalk.com/robot/send?access_token=your_token' #用你的实际token替换your_token
#     xiaoding = DingtalkChatbot ( webhook )
#     xiaoding.send_text (
#         msg="《{}》已生成，有 {} 个异常用例！请用浏览器打开查看详情，链接是：{}".format(driver.title ,fail_text,test_reports_url))else:
#     print('《{}》已生成，无异常用例，很棒！'.format(driver.title))# 关闭浏览器driver.quit()
