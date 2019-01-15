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


class Vehicles_Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("车辆测试开始")

    def test_vehicles_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicles"
        params = {
            "page": "1",
            "size": 20
        }
        headers = {
           'accept': 'application/json',
           'Content-Type': 'application/json'
        }
        response = requests.get(url, params, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_vehicles_post(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicles"
        body = {
           "boxId": 203910239,
           "businessLine": {
           "areaCode": 350603,
           "plan": False,
           "planBackTime": 10800,
           "planDepartureTime": 10800,
           "test": False,
           "typeId": 1
          },
           "buyDate": 1541518953756,
           "engineModel": "HL0001",
           "idNumber": "ABCDEFGHIJKLMNOPQ",
           "plateNumber": "闽Y88888"
        }
        headers = {
            'accept': 'application/json'
        }
        response1 = requests.post(url, '', json=body, headers=headers)
        print(response1.status_code)
        print(response1.url)
        print(response1.json())
        self.assertEqual(response1.status_code, 200)

    def test_vehicles_put(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicles"+"/"+"43"
        body = {
              "boxId": 293819231,
              "businessLine": {
                  "areaCode": 350603,
                  "plan": False,
                  "planBackTime": 10800,
                  "planDepartureTime": 10800,
                  "test": False,
                  "typeId": 1
                },
              "buyDate": 1541518953756,
              "engineModel": "HL0002",
              "idNumber": "ABCDEFGHIJKLMNOPQ",
              "plateNumber": "闽Y88888",
              "state": "UnAvailable"
         }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response2 = requests.put(url, json=body, headers=headers)
        print(response2.status_code)
        print(response2.url)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)

    def test_vehicle_delete(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicles"+"/"+"58"
        headers = {
            'accept': 'application/json'
        }
        response3 = requests.delete(url, headers=headers)
        print(response3.status_code)
        print(response3.url)
        print(response3.json())
        self.assertEqual(response3.status_code, 200)




    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()