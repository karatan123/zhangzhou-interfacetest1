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
class ReportvehicleinspectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("后端出车检查相关报表测试开始")
        #     获取权限
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
        #   正则提取需要的token值
        global token
        s1 = response.json()
        token = s1["data"]["token"]
        print(token)


#获取出车检查分页数据
    def test_reportvehicleinspection_month_get(self):
        month = "2019-04"
        url = "http://125.94.39.168:8888/api/reports/vehicleInspection/" + month
        data = {
            'page': 1,
            'size': 20
        }
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, params=data, headers=headers)
        print(response.url)
        print(response.headers)
        self.assertEqual(response.status_code, 200)

#导出出车检查分页数据
    def test_reportvehicleinspection_export_month_get(self):
        month = "2019-04"
        url = "http://125.94.39.168:8888/api/reports/vehicleInspection/export/" + month
        data = {
            'page': 1,
            'size': 20
        }
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, params=data, headers=headers)
        print(response.url)
        print(response.headers)
        self.assertEqual(response.status_code, 200)





    @classmethod
    def tearDownClass(self):
            print(u"后端出车检查相关报表测试开始！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()