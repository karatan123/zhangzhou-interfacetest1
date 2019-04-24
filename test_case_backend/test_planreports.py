#!/usr/bin/env python
#coding: utf-8
'''
unittest interface
@author: kara
@version: 1.0
@see:http://www.python-requests.org/en/master/
'''

import unittest
import json
import traceback
import requests
import time

token = ''
class PlanreportsTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("后端方案报表接口测试开始")
    #     获取权限
        url = "http://recycling.3po-dwm.com:8888/api/auth"
        body = {
           "password": "123456",
           "username": "zhangzhou1012"
        }
        headers = {
           'accept': '*/*',
           'Content-Type': 'application/json'
        }
        response = requests.post(url, '', body, headers=headers)
        print(response.status_code)
        print(response.headers)
        print(response.json())
    #   正则提取需要的token值
        global token
        s1 = response.json()
        token = s1["data"]["token"]
        print(token)

    def test_planreports_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/reports/plans" + "/" + "349"
        headers = {
            "accept":'*/*',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, headers=headers)
        print(response.url)
        print(response.headers)
        self.assertEqual(response.status_code, 200)




    @classmethod
    def tearDownClass(self):
            print(u"后端方案报表接口测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()