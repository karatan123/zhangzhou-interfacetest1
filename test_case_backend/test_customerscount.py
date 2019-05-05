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
class CustomerscountTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("后端收运单位统计接口测试开始")
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

    #根据收运单位id和月份查询收运明细
    def test_customerscount_byidanmonth_get(self):
        customerid = "201825"
        month = "2019-04"
        url = "http://recycling.3po-dwm.com:8888/api/customerCounts/" + customerid + "/" + month
        headers = {
            'accept': '*/*',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url,headers=headers)
        print(response.url)
        print(response.json())
        print(response.headers)
        self.assertEqual(response.status_code, 200)

    #导出收运单位当月的收运明细
    def test_customerscount_exportbyidandmonth_get(self):
        customerid = "201825"
        month = "2019-04"
        url = "http://recycling.3po-dwm.com:8888/api/customerCounts/export/" + customerid + "/" + month
        headers = {
            'accept': 'application/pdf',
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, headers=headers)
        print(response.url)
        print(response.headers)
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(self):
            print(u"后端收运单位统计接口测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()