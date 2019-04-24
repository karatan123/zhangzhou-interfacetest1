#!/usr/bin/env python
#coding: utf-8
'''
unittest interface
@author: kara
@version: 1.0
@see:
'''

import unittest
import json
import traceback
import requests
import time

token = ''
class Auth2Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("收运端权限测试开始")

    def test_auth2_post(self):
        url = "http://recycling.3po-dwm.com:9999/api/auth"
        body = {
          "attendant1": 123698,
          "attendant2": 123543,
          "driver": 123687,
          "vehicle": 105
        }
        headers = {
           'accept': 'application/json',
           'Content-Type': 'application/json'
        }
        response = requests.post(url, '', body, headers=headers)
        print(response.status_code)
        print(response.url)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        #   正则提取需要的token值
        global token
        s1 = response.json()
        token = s1["data"]["token"]
        print(token)

    def test_auth2_get(self):
        global token
        url = "http://recycling.3po-dwm.com:9999/api/refresh"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, headers=headers)
        print(response.status_code)
        print(response.url)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_auth2_logout_post(self):
        url = "http://recycling.3po-dwm.com:9999/api/auth/signOut"
        body = {
          "driver": 123687,
          "vehicle": 105
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.post(url, json=body, headers=headers)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)


    @classmethod
    def tearDownClass(self):
            print(u"收运端权限测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()