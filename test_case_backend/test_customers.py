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

postid = 0
class CustomersTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("收运单位测试开始")

    def test_customers_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/customers"
        params = {
            "page": 1,
            "size": 20
        }
        headers = {
           'accept': 'application/json'
        }
        response = requests.get(url, params=params, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_customers_post(self):
        url = "http://recycling.3po-dwm.com:8888/api/customers"
        body = {
            "address": {
                "cityCode": 350600,
                "countyCode": 350603,
                "detailedAddress": "中山路红绿灯交界",
                "lat": 23.123123,
                "lng": 123.123123,
                "provinceCode": 350000,
                "streetCode": 350603100
             },
            "category": "Separate",
            "collectionPeriodList": [
               {
                "dateType": "Working",
                "endTime": 10800,
                "garbageCategory": "KitchenWaste",
                "id": 1,
                "plateNumber": "闽Y88888",
                "priorityType": "Hard",
                "startTime": 10800
               }
             ],
            "contactInfo": {
                "contactName": "曹操",
                "landlinePhone": "020-85111260",
                "mobilePhone": 16888888888
             },
            "customerList": [
                {
                    "name": "小曼十香"
                }
            ],
            "dustbin": 10,
            "name": "万达广场123",
            "needKey": True,
            "password": "admin",
            "typeId": 1,
            "username": "admin"
         }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response1 = requests.post(url, '', json=body, headers=headers)
        print(response1.url)
        print(response1.status_code)
        print(response1.headers)
        print(response1.json())
        self.assertEqual(response1.status_code, 200)
        #     第三步：正则提取需要的参数值
        global postid
        s = response1.json()
        postid = s["data"]["id"]
        print(postid)

    def test_customers_put(self):
        global postid
        url = "http://125.94.39.168:8888/api/customers" + "/" + str(postid)
        body = {
            "address": {
               "cityCode": 350600,
               "countyCode": 350603,
               "detailedAddress": "中山路红绿灯交界",
               "lat": 23.123123,
               "lng": 123.123123,
               "provinceCode": 350000,
               "streetCode": 350603100
             },
            "category": "Cluster",
            "collectionPeriodList": [
             {
               "dateType": "Working",
               "endTime": 10800,
               "garbageCategory": "KitchenWaste",
               "id": 1,
               "plateNumber": "粤Y88888",
               "priorityType": "Hard",
               "startTime": 10800
               }
              ],
             "contactInfo": {
                "contactName": "曹操",
                "landlinePhone": "020-85111260",
                "mobilePhone": 16888888888
              },
             "customerList": [
               {
                "id": postid+1,
                "name": "小曼十香123"
               }
             ],
            "dustbin": 10,
            "name": "万达广场",
            "needKey": True,
            "password": "",
            "typeId": 1,
            "username": ""
         }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response3 =requests.put(url, json=body, headers=headers)
        print(response3.url)
        print(response3.status_code)
        print(response3.headers)
        print(response3.json())
        self.assertEqual(response3.status_code, 200)

    # 添加子收运点
    def test_customers_separatepost(self):
        global postid
        url = "http://125.94.39.168:8888/api/customers" + "/" + str(postid)
        body = [
             {
              "name": "小草"
            }
         ]
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response5 = requests.post(url, '', json=body, headers=headers)
        print(response5.url)
        print(response5.status_code)
        print(response5.headers)
        print(response5.json())
        self.assertEqual(response5.status_code, 200)

    def test_customer_delete(self):
        global postid
        url = "http://125.94.39.168:8888/api/customers" + "/" + str(postid)
        headers = {
            'accept': 'application/json'
        }
        response4 = requests.delete(url, headers=headers)
        print(response4.url)
        print(response4.status_code)
        print(response4.headers)
        print(response4.json())
        self.assertEqual(response4.status_code, 200)



    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()