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
class FuelrecordTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("司机端加油记录测试开始")
        #     获取权限
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
        print(response.headers)
        print(response.json())
        #   正则提取需要的token值
        global token
        s1 = response.json()
        token = s1["data"]["token"]
        print(token)

    def test_fuelrecord_post(self):
        url = "http://recycling.3po-dwm.com:9999/api/fuels/record"
        body = {
              "capacity": 150,
              "cardBalance": 10.5,
              "fillMoney": 500,
              "lat": 23.123123,
              "lng": 123.123123,
              "mileage": 0,
              "money": 200,
              "routeId": 474
            }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.post(url, json=body, headers=headers)
        print(response.status_code)
        print(response.url)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)



    @classmethod
    def tearDownClass(self):
            print(u"司机端加油记录测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()