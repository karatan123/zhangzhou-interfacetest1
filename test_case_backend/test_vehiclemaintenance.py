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
postid = ''
class VehiclemaintenanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("后端车辆维修记录接口测试开始")
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

    def test_vehiclemaintenance_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicleMaintenance?page=1&size=20&sort=maintenanceStartTime.desc%2CplateNumber.desc"
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, headers=headers)
        print(response.status_code)
        print(response.json())
        print(response.headers)
        self.assertEqual(response.status_code, 200)

    def test_vehiclemaintenance_post(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicleMaintenance"
        body = {
              "acceptancePerson": "kara",
              "maintenanceCompany": "一德汽修厂",
              "maintenanceContent": "更换发动机",
              "maintenanceCost": 99.98,
              "maintenanceEndTime": 1541518953756,
              "maintenanceMileage": 9981,
              "maintenanceReasons": "发动机漏油",
              "maintenanceStartTime": 1541518953756,
              "plateNumber": "闽8001",
              "sendPerson": "张三",
              "vehicleId": 105
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.post(url, json=body, headers=headers)
        print(response.status_code)
        print(response.json())
        print(response.headers)
        self.assertEqual(response.status_code, 200)
        #正则提取创建的维修记录的id
        global postid
        s1 = response.json()
        postid = s1["data"]["id"]
        print(postid)

    def test_vehiclemaintenance_put(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicleMaintenance" + "/" + str(postid)
        body = {
              "acceptancePerson": "kara",
              "maintenanceCompany": "一德汽修厂",
              "maintenanceContent": "维修发动机",
              "maintenanceCost": 99.98,
              "maintenanceEndTime": 1541518953756,
              "maintenanceMileage": 10000,
              "maintenanceReasons": "发动机漏油",
              "maintenanceStartTime": 1541518953756,
              "plateNumber": "闽8001",
              "sendPerson": "张三",
              "vehicleId": 105
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

    def test_vehiclemaintenance_delete(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicleMaintenance" + "/" + str(postid)
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.delete(url, headers=headers)
        print(response.status_code)
        print(response.url)
        print(response.json())
        print(response.headers)
        self.assertEqual(response.status_code, 200)

    def test_vehiclemaintenance_export_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/vehicleMaintenance/export?page=1&size=20&sort=maintenanceStartTime.desc%2CplateNumber.desc"
        headers = {
            'accept': '*/*',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, headers=headers)
        print(response.status_code)
        print(response.url)
        print(response.headers)
        self.assertEqual(response.status_code, 200)





    @classmethod
    def tearDownClass(self):
            print(u"后端车辆维修记录接口测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()