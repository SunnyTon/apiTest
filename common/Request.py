# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 15:35
# @Author  : SunnyTang
# @FileName: Request.py
def post_request(self, url, data, header):
    """
    Post请求
    :param url:
    :param data:
    :param header:
    :return:

    """
    if not url.startswith('http://'):
        url = '%s%s' % ('http://', url)
        print(url)
    try:
        if data is None:
            response = self.get_session.post(url=url, headers=header)
        else:
            response = self.get_session.post(url=url, params=data, headers=header)

    except requests.RequestException as e:
        print('%s%s' % ('RequestException url: ', url))
        print(e)
        return ()

    except Exception as e:
        print('%s%s' % ('Exception url: ', url))
        print(e)
        return ()

    # time_consuming为响应时间，单位为毫秒
    time_consuming = response.elapsed.microseconds / 1000
    # time_total为响应时间，单位为秒
    time_total = response.elapsed.total_seconds()

    Common.Consts.STRESS_LIST.append(time_consuming)

    response_dicts = dict()
    response_dicts['code'] = response.status_code
    try:
        response_dicts['body'] = response.json()
    except Exception as e:
        print(e)
        response_dicts['body'] = ''

    response_dicts['text'] = response.text
    response_dicts['time_consuming'] = time_consuming
    response_dicts['time_total'] = time_total

    return response_dicts