# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 15:30
# @Author  : SunnyTang
# @FileName: Assert.py
def assert_body(self, body, body_msg, expected_msg):
    """
    验证response body中任意属性的值
    :param body:
    :param body_msg:
    :param expected_msg:
    :return:
    """
    try:
        msg = body[body_msg]
        assert msg == expected_msg
        return True

    except:
        self.log.error(
            "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
        Consts.RESULT_LIST.append('fail')

        raise


def assert_in_text(self, body, expected_msg):
    """
    验证response body中是否包含预期字符串
    :param body:
    :param expected_msg:
    :return:
    """
    try:
        text = json.dumps(body, ensure_ascii=False)
        # print(text)
        assert expected_msg in text
        return True

    except:
        self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
        Consts.RESULT_LIST.append('fail')

        raise
