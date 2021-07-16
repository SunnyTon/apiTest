# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 15:39
# @Author  : SunnyTang
# @FileName: tools.py
class Basic:
    params = get_parameter('Basic')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])