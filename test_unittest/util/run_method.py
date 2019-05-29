#!/usr/bin/python
# coding=utf-8
# 作者      :BuYang
# 创建时间  :2019/5/16 10:55
# 文件      :run_method.py
# IDE       :PyCharm
import requests


class RunMethod(object):

    def post_method(self, url, data, header=None):
        if header is not None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def get_method(self, url, data, header=None):
        if header is not None:
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, params=data, verify=False)
        return res.json()
