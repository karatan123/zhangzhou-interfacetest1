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
class Auth1Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("手持管理端权限测试开始")

    def test_auth_post(self):
        url = "http://recycling.3po-dwm.com:7777/api/auth"
        body = {
            "password": "123456",
            "username": "zhangzhou1012"
        }
        headers = {
           'accept': 'application/json',
           'Content-Type': 'application/json'
        }
        response = requests.post(url, '', body, headers=headers)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        #   正则提取需要的token值
        global token
        s1 = response.json()
        token = s1["data"]["token"]
        print(token)

    def test_auth_get(self):
        global token
        url = "http://recycling.3po-dwm.com:7777/api/refresh"
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.request("GET", url, headers=headers)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(self):
            print(u"手持管理端权限测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()