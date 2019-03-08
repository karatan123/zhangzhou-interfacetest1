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
import random
import string

postid = 0
token = ''
plate_num = ''
idnum = ''
boxid = ''

class Vehicles_Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("车辆测试开始")
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

    def test_vehicles_get(self):
        global token
        url = "http://recycling.3po-dwm.com:8888/api/vehicles"
        params = {
            "page": "1",
            "size": 20
        }
        headers = {
           'accept': 'application/json',
           'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, params, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_vehicles_post(self):
        global token
        global plate_num
        global idnum
        global boxid
        # 车牌号、车架号、车载盒子id具有唯一性，通过随机数生成
        num1 = random.randint(00000, 99999)
        plate_num = "闽Y" + str(num1)
        print(plate_num)

        num2 = random.sample(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], 17)
        idnum = num2[0] + num2[1] + num2[2]+ num2[3]+ num2[4]+ num2[5]+ num2[6]+ num2[7]+ num2[8]+ num2[9]+ num2[10]+ num2[11]+ num2[12]+ num2[13]+ num2[14]+ num2[15]+ num2[16]
        print(idnum)

        boxid = "1" + str(random.randint(10000000, 99999999))
        print(boxid)


        url = "http://recycling.3po-dwm.com:8888/api/vehicles"
        body = {
           "boxId": boxid,
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
           "idNumber": idnum,
           "plateNumber": plate_num
        }
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
        }
        response1 = requests.post(url, '', json=body, headers=headers)
        print(response1.status_code)
        print(response1.url)
        print(response1.json())
        self.assertEqual(response1.status_code, 200)
        #     第三步：正则提取需要的参数值postid
        global postid
        s = response1.json()
        postid = s["data"]["id"]
        print(postid)

    def test_vehicles_put(self):
        global token
        global plate_num
        global idnum
        global boxid
        global postid
        # 重新生成車架號
        num2 = random.sample(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'], 17)
        idnum = num2[0] + num2[1] + num2[2] + num2[3] + num2[4] + num2[5] + num2[6] + num2[7] + num2[8] + num2[9] + \
                num2[10] + num2[11] + num2[12] + num2[13] + num2[14] + num2[15] + num2[16]
        print(idnum)

        url = "http://recycling.3po-dwm.com:8888/api/vehicles"+"/"+str(postid)
        body = {
           "boxId": boxid,
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
           "idNumber": idnum,
           "plateNumber": plate_num
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token
        }
        response2 = requests.put(url, json=body, headers=headers)
        print(response2.status_code)
        print(response2.url)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)

    def test_vehicle_delete(self):
        global token
        global postid
        url = "http://recycling.3po-dwm.com:8888/api/vehicles"+"/"+str(postid)
        headers = {
            'accept': 'application/json',
            "Authorization": "Bearer " + token
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