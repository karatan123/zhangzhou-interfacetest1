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
from requests_toolbelt import MultipartEncoder


postid = 0
token = ''
class CustomersTest1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("手持机管理收运单位测试开始")
        #     获取权限
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
        #   正则提取需要的token值
        global token
        s1 = response.json()
        token = s1["data"]["token"]
        print(token)

    def test_customers_get(self):
        global token
        url = "http://recycling.3po-dwm.com:7777/api/customers"
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
        url = "http://recycling.3po-dwm.com:7777/api/customers"
        body = {
                "address": {
                    "cityCode": 350600,
                    "countyCode": 350603,
                    "detailedAddress": "福建省漳州市龙文区蓝田镇xxx",
                    "lat": 23.123123,
                    "lng": 123.123123,
                    "provinceCode": 350000,
                    "streetCode": 350603100
                },
                "category": "Separate",
                "customerList": [
                    {
                        "name": "御品牛肉"
                    }
                ],
                "name": "浪漫广场",
                "typeId": 1
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

    # 根据收运单位 id 查询收运单位信息
    def test_customers_id_get(self):
        global token
        url = "http://recycling.3po-dwm.com:7777/api/customers" + "/" + str(postid)
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response2 = requests.get(url, '', headers=headers)
        print(response2.url)
        print(response2.status_code)
        print(response2.headers)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)

    def test_customers_put(self):
        global postid
        global token
        url = "http://125.94.39.168:7777/api/customers" + "/" + str(postid)
        body = {
            "address": {
                 "cityCode": 350600,
                 "countyCode": 350603,
                 "detailedAddress": "福建省漳州市龙文区蓝田镇xxx",
                 "lat": 23.123123,
                 "lng": 123.123123,
                 "provinceCode": 350000,
                 "streetCode": 350603100
             },
            "category": "Separate",
            "customerList": [
               {
                "id": postid+1,
                "name": "御品牛肉123"
              }
             ],
            "imageIds": [
               1,
               2
            ],
            "name": "浪漫广场123",
            "typeId": 1
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

        # 收运单位绑卡
    def test_customers_RFID_post(self):
        global postid
        global token
        url = "http://recycling.3po-dwm.com:7777/api/customers/" + str(postid + 1) + "/rfids/" + "659670805" + "/00000"
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response5 = requests.post(url, '', '', headers=headers)
        print(response5.url)
        print(response5.status_code)
        print(response5.headers)
        print(response5.json())
        self.assertEqual(response5.status_code, 200)

    # 收运单位解绑
    def test_customers_RFID_delete(self):
        global postid
        global token
        url = "http://recycling.3po-dwm.com:7777/api/customers/" + str(postid + 1) + "/rfids/" + "659670805"
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response6 = requests.delete(url, headers=headers)
        print(response6.url)
        print(response6.status_code)
        print(response6.headers)
        print(response6.json())
        self.assertEqual(response6.status_code, 200)

    # 上传收运单位或聚类点的图片
    def test_customers_uploadimages_post(self):
        global token
        global postid
        # url = "http://recycling.3po-dwm.com:7777/api/customers/" + str(postid) + "/images"
        url = "http://125.94.39.168:7777/api/customers/201225/images"
        headers = {
            'accept': 'application/json',
            'Content-Type': "multipart/form-data; boundary=----WebKitFormBoundaryFsbnOAOXweGMsjT3",
            # 'Content-Type': "application / octet - stream",
            "Authorization": "Bearer " + token
        }
        # 创建form data形式数据  主要是针对上传文件
        multipart_encoder = MultipartEncoder(
            fields={
                # 这里根据服务器需要的参数格式进行修改
                # "description": u"测试数据",
                # "version": 0.1,
                'images': ('dashboard.png', open('/Users/kara/dashboard.png', 'rb'), 'image/png')
            },

        )
        response7 = requests.post(url, data=multipart_encoder, headers=headers)
        print(url)
        print(response7.status_code)
        print(response7.headers)
        print(response7.json())
        self.assertEqual(response7.status_code, 200)

    def test_customers_delete(self):
        global postid
        global token
        url = "http://recycling.3po-dwm.com:7777/api/customers" + "/" + str(postid)
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

    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()