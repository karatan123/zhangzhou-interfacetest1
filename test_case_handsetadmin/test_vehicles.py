
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
from urllib import parse
from urllib.request import urlopen

class VehiclesTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("手持机管理员工测试开始")

    # 车辆分页查询
    def test_vehicles_get(self):
        url = "http://recycling.3po-dwm.com:7777/api/vehicles"
        params = {
            "plateNumber": "闽Y"
        }
        headers = {
            'accept': 'application/json'
        }
        response = requests.get(url, params=params, headers=headers)
        print(response.url)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    # 车辆绑卡
    def test_vehicle_RFID_post(self):
        url = "http://recycling.3po-dwm.com:7777/api/vehicles" +"/" +"42" +"/rfids/" +"1206534649"
        headers = {
            'accept': 'application/json'
        }
        response1 = requests.post(url, '', '', headers=headers)
        print(response1.url)
        print(response1.headers)
        print(response1.json())
        self.assertEqual(response1.status_code, 200)

        # 车辆绑卡
    def test_vehicle_RFID_delete(self):
        url = "http://recycling.3po-dwm.com:7777/api/vehicles" + "/" + "42" + "/rfids/" + "1206534649"
        headers = {
            'accept': 'application/json'
        }
        response2= requests.delete(url, headers=headers)
        print(response2.url)
        print(response2.headers)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)

    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()