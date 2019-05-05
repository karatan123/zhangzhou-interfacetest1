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
postid = 0
postid1 = 0 #虚拟任务即台账新增加任务的id
class CustomersTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("收运单位测试开始")
        #      获取token
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

    def test_customers_get(self):
        global token
        url = "http://recycling.3po-dwm.com:8888/api/customers"
        params = {
            "page": 1,
            "size": 20
        }
        headers = {
           'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, params=params, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_customers_post(self):
        global token
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
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
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

            # 根据ID查询收运单位信息
    def test_customers_byid_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/customers/" + str(postid)
        headers = {
            'accept': '*/*',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

#更新收运单位位置信息
    def test_customers_location_put(self):
        url = "http://recycling.3po-dwm.com:8888/api/customers/" + str(postid+1) +"/location"
        body = {
          "lat": 23.123123,
          "lng": 123.123123
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.put(url, json=body, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

       #创建子收运单位
    def test_customers_subcustomer_post(self):
        url = "http://recycling.3po-dwm.com:8888/api/customers/" + str(postid)
        body = [
          {
            "name": "万达广场下的子点面食王"
          }
        ]
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.post(url, json=body, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_customers_put(self):
        global token
        global postid
        url = "http://recycling.3po-dwm.com:8888/api/customers" + "/" + str(postid)
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
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response3 =requests.put(url, json=body, headers=headers)
        print(response3.url)
        print(response3.status_code)
        print(response3.headers)
        print(response3.json())
        self.assertEqual(response3.status_code, 200)

    # 添加子收运点
    def test_customers_separatepost(self):
        global token
        global postid
        url = "http://recycling.3po-dwm.com:8888/api/customers" + "/" + str(postid)
        body = [
             {
              "name": "小草"
            }
         ]
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response5 = requests.post(url, '', json=body, headers=headers)
        print(response5.url)
        print(response5.status_code)
        print(response5.headers)
        print(response5.json())
        self.assertEqual(response5.status_code, 200)

    #子收运点变为普通收运点
    def test_customers_leavecluster_put(self):
        url = "http://recycling.3po-dwm.com:8888/api/customers/leaveCluster"
        body = [
            postid+1
        ]
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.put(url, json=body, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    #普通收运点加入聚类点
    def test_customers_joincluster_put(self):
        url = "http://125.94.39.168:8888/api/customers/joinCluster/" + str(postid)
        body = [
            postid+1
        ]
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.put(url, json=body, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_customer_delete(self):
        global token
        global postid
        url = "http://recycling.3po-dwm.com:8888/api/customers" + "/" + str(postid)
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response4 = requests.delete(url, headers=headers)
        print(response4.url)
        print(response4.status_code)
        print(response4.headers)
        print(response4.json())
        self.assertEqual(response4.status_code, 200)

#查询收运单位异常情况
    def test_customers_exeptions_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/customers/exceptions?page=1&size=20"
        data = {
            'month': "2019-04",
            'page': 1,
            'size': 20
        }
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, params=data, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    #导出收运单位异常情况
    def test_customers_reportbymonthandstreet_get(self):
        month = "2019-04"
        street = "350603100"
        url = "http://recycling.3po-dwm.com:8888/api/customers/exceptions/reports/" + month + "/" + street
        headers = {
            'accept': '*/*',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        self.assertEqual(response.status_code, 200)


    #增加虚拟收集任务即台账的添加功能
    def test_customers_addvirtualtask_post(self):
        url = "http://recycling.3po-dwm.com:8888/api/customers/addVirtualTask"
        body = {
          "collectionTime": 1541518953756,
          "customerId": 201825,
          "customerName": "桂城中学",
          "driverId": 123520,
          "quantity": 0.3,
          "type": "VIRTUAL",
          "vehicleId": 96
        }

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.post(url, json=body, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.json())
        print(response.headers)
        self.assertEqual(response.status_code, 200)
        s = response.json()
        global postid1
        postid1 = s["data"]["id"]

    #更新收集任务信息
    def test_customers_updatetask_put(self):
        url = 'http://recycling.3po-dwm.com:8888/api/customers/updateTask'
        body = {
          "collectionTime": 1541518953756,
          "driverId": 123520,
          "quantity": 0.5,
          "taskId": postid1,
          "type": "VIRTUAL",
          "vehicleId": 96
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.put(url, json=body, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        self.assertEqual(response.status_code, 200)

    #删除虚拟收集任务信息
    def test_customers_virtualtaskbyid_delete(self):
        url = "http://125.94.39.168:8888/api/customers/virtualTask/" + str(postid1)
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.delete(url, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        self.assertEqual(response.status_code, 200)








    @classmethod
    def tearDownClass(self):
            print(u"收运单位测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()