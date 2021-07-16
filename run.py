# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pytest


# if __name__ == '__main__':
#     # 指定运行单个测试目录
#     pytest.main(['./case/login.py'])
if __name__ == '__main__':
        # 定义测试集
        #self_args = sys.argv[1:]
        pytest.main(['-s', '-q', '--alluredir', './report/result','./cases/test_activitybullish_flipcard.py'])
        #自动执行
        cmd = 'allure generate %s -o %s' % ('report/result', 'report/html')
        #手动执行
        # -> cd C:\Users\Administrator\PycharmProjects\apiTest\report>
        # -> allure generate ./result/ -o ./html --clean

        # try:
        #         shell.invoke(cmd)
        # except:
        #         log.error('执行用例失败，请检查环境配置')
        #         raise
        #
        # try:
        #         mail = Email.SendMail()
        #         mail.sendMail()
        # except:
        #         log.error('发送邮件失败，请检查邮件配置')
        #         raise