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


class AuthTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("权限测试开始")

    def test_auth_post(self):
        url = "http://125.94.39.168:8888/api/auth"
        body = {
            "password": "123456",
            "username": "zhangzhou6605"
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

    def test_auth_get(self):
        url = "http://125.94.39.168:8888/api/refresh"
        headers = {
            'accept': 'application/json'
        }
        response = requests.request("GET", url, headers=headers)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()