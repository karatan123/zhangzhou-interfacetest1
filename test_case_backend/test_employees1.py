#!/usr/bin/env python
#coding: utf-8
'''
unittest interface
@author: kara
@version: 1.0
@see:http://www.python-requests.org/en/master/
'''
'''参数放在url后用data或params，json一般都是传body参数，query类型是将参数放在url中，path是直接改变url'''

import unittest
import json
import traceback
import requests
import time
import re
import os
import random
import string

postid = 0
username = ""
phone = ""
identity = ""

class EmployeesTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("人员测试开始")

    def test_employees_post(self):
        url = "http://recycling.3po-dwm.com:8888/api/employees"
        num1 = random.randint(1000, 9999)
        global username
        username = "testerkara" + str(num1)
        print(username)

        num2 = random.randint(70000000, 79999999)
        global phone
        phone = "186" + str(num2)
        print(phone)

        num3 = random.randint(100000, 999999)
        num4 = random.randint(1000, 9999)
        global identity
        identity = str(num3) + "19900101" + str(num4)
        print(identity)
        body = {
              "address": {
                 "city": "漳州市",
                 "cityCode": 350600,
                 "county": "龙文区",
                 "countyCode": 350603,
                 "detailedAddress": "福建省漳州市龙文区蓝田镇xxx",
                 "homeAddress": "福建省漳州市龙文区蓝田镇xxx",
                 "province": "福建省",
                 "provinceCode": 350000,
                 "street": "蓝田镇",
                 "streetCode": 350603100
              },
              "contactInfo": {
                 "email": "yuningli@locision.com",
                 "emergencyContact": "李白",
                 "emergencyContactPhone": 15888888889,
                 "landlinePhone": "0754-85111260",
                 "mobilePhone": phone
              },
              "entryTime": 1541556456399,
              "identity": identity,

              "name": "张三",
              "password": "admin",
              "postId": 2,
              "roles": [
                1
              ],
              "sex": "Male",
              "username": username
         }
        headers = {
             'accept': '*/*',
             'Content-Type': 'application/json'
         }
        response = requests.post(url, '', json=body, headers=headers)
        print(url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
    #     第三步：正则提取需要的参数值
        global postid
        s = response.json()
        postid = s["data"]["id"]
        print(postid)

    def test_employees_put(self):
        global postid
        global username
        global phone
        global identity
        url = "http://recycling.3po-dwm.com:8888/api/employees" + "/" + str(postid)
        body = {
            "address": {
                "city": "漳州市",
                "cityCode": 350600,
                "county": "龙文区",
                "countyCode": 350603,
                "detailedAddress": "福建省漳州市龙文区蓝田镇xxx",
                "homeAddress": "福建省漳州市龙文区蓝田镇xxx",
                "province": "福建省",
                "provinceCode": 350000,
                "street": "蓝田镇",
                "streetCode": 350603100
            },
            "contactInfo": {
                "email": "yuningli@locision.com",
                "emergencyContact": "李白",
                "emergencyContactPhone": 15888888889,
                "landlinePhone": "0754-85111260",
                "mobilePhone": phone
            },
            "entryTime": 1541556456399,
            "identity": identity,

            "name": "张三",
            "password": "admin",
            "postId": 2,
            "roles": [
                1
            ],
            "sex": "Male",
            "username": username
        }
        headers = {
            'accept': '*/*',
            'Content-Type': 'application/json'
        }
        response2 = requests.put(url, json=body, headers=headers)
        print(response2.url)
        print(response2.content)
        print(response2.status_code)
        print(response2.headers)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)


    def test_employees_delete(self):
        global postid
        url = os.path.join("http://125.94.39.168:8888/api/employees"+"/"+str(postid))
        headers = {
             'accept': '*/*'
        }
        response2 = requests.delete(url, headers=headers)
        print(url)
        print(response2.status_code)
        print(response2.headers)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)

    # 分页查询
    def test_employees_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/employees"
        headers = {
            'accept': '*/*'
        }
        params = {
            "page": 1,
            "size": 20,
            "username": "admin"
        }
        response = requests.get(url, params, headers=headers)
        self.assertEqual(response.status_code, 200)
        print(response.json())


    @classmethod
    def tearDown(self):
            print(u"自动测试完毕！")


# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()
