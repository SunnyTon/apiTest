▷  apiTest
apiTest框架基于Python3+pytest+requests+allure组成，通过接口测试用例模板编写用例。

这套框架分为二层：业务用例层、数据层；项目目录分为9层。
对断言、requests、钉钉报告、日志进行了封装。
适用于数据驱动、关键字驱动。

本例子展示了一个了618抽卡部分功能接口自动化Demo。

▷  框架亮点
❤️支持用例重跑及日志反馈
❤️使用allure美化html报告，包含用例等级，说明
❤️支持钉钉自动发送测试报告
❤️支持mysql读取数据
*后期优化
❤️集成Jenkins，使用Jenkins插件生成Allure报告
❤️多线程并发接口自动化测试
❤️接口加密，参数加密

目录结构
--bin目录，用于存放启动文件，如run.py
|
--cases目录，存放测试脚本
|
--config目录，存放各种路径配置、服务器接口配置等等
|
--common目录，放通用文件
|
--testdata，YAML文件，存放case的data数据文件
|
--lib，存放各种附加的代码文件，如加密、链接数据库、生成测试脚本等
|
--report目录，存放测试报告
|
--test目录，单元测试文件
|
--case_template.txt，模板文件，生成测试脚本的模板
