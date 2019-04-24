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
postid = 0
class VehicleupkeepTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("后端车辆保养记录接口测试开始")
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

    def test_vehicleupkeep_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicleUpkeep"
        params = {
            "page": 1,
            'size': 20
        }
        headers = {
            'accept':'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, params=params, headers=headers)
        print(response.status_code)
        print(response.url)
        print(response.json())
        print(response.headers)
        self.assertEqual(response.status_code, 200)

    def test_vehicleupkeep_post(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicleUpkeep"
        body = {
              "acceptancePerson": "赵五",
              "chargePerson": "李四",
              "planUpkeepTime": 1541518953756,
              "plateNumber": "闽Y88888",
              "upkeepCompany": "一德汽修厂",
              "upkeepContent": "打黄油",
              "upkeepCost": 99.99,
              "upkeepMileage": 9981,
              "upkeepPerson": "张三",
              "upkeepTime": 1541518953756,
              "upkeepTimeCost": 9981,
              "vehicleId": 43
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.post(url, json=body, headers=headers)
        print(response.status_code)
        print(response.url)
        print(response.json())
        print(response.headers)
        self.assertEqual(response.status_code, 200)
        # 正则提取创建的保养记录的id
        global postid
        s1 = response.json()
        postid = s1["data"]["id"]
        print(postid)

    def test_vehicleupkeep_put(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicleUpkeep" + "/" + str(postid)
        body = {
              "acceptancePerson": "kara",
              "chargePerson": "李四",
              "planUpkeepTime": 1541518953756,
              "plateNumber": "闽Y88888",
              "upkeepCompany": "一德汽修厂",
              "upkeepContent": "打黄油",
              "upkeepCost": 99.99,
              "upkeepMileage": 9981,
              "upkeepPerson": "张三",
              "upkeepTime": 1541518953756,
              "upkeepTimeCost": 9981,
              "vehicleId": 43
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.put(url, json=body, headers=headers)
        print(response.status_code)
        print(response.url)
        print(response.json())
        print(response.headers)
        self.assertEqual(response.status_code, 200)

    def test_vehicleupkeep_delete(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicleUpkeep" + "/" +str(postid)
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.delete(url, headers=headers)
        print(response.status_code)
        print(response.url)
        print(response.json())
        print(response.headers)
        self.assertEqual(response.status_code, 200)

    def test_vehicleupkeep_export_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicleUpkeep/export"
        params = {
            'page': 1,
            'size': 20
        }
        headers = {
            'accept': '*/*',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, params=params, headers=headers)
        print(response.status_code)
        print(response.url)
        print(response.headers)
        self.assertEqual(response.status_code, 200)


    @classmethod
    def tearDownClass(self):
            print(u"后端车辆保养记录接口测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()