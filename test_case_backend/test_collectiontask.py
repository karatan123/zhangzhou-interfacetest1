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

postid =0
class CollectiontaskTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("后端收运请求测试开始")

    def test_collectiontask_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/tasks"
        params = {
            "page": 1,
            "size": 20
        }
        headers = {
            "accept": "*/*"
        }
        response = requests.get(url, params=params, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_collectiontask_post(self):
        url = "http://recycling.3po-dwm.com:8888/api/tasks"
        body = [
                 {
                 "amountOfGarbage": 2.5,
                 "collectionPeriodId": 44,
                 "customerId": 201241,
                 "name": "东方大广场",
                 "subTaskList": [
                  {
                  "amountOfGarbage": 2.5,
                  "customerId": 201242,
                  "name": "重庆火锅"
                  }
                 ]
               }
         ]
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }
        response1 = requests.post(url, json=body, headers=headers)
        print(response1.url)
        print(response1.status_code)
        print(response1.json())
        self.assertEqual(response1.status_code, 200)
        #     第三步：正则提取需要的参数值收运请求id
        global postid
        s1 = response1.json()
        postid = s1["data"][0]["id"]
        print(postid)

    def test_collectiontask_put(self):
        global postid
        url = "http://recycling.3po-dwm.com:8888/api/tasks/" + str(postid)
        body = {
             "amountOfGarbage": 2.4,
             "collectionPeriodId": 44
        }
        heades = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }
        response2 = requests.put(url, json=body, headers=heades)
        print(response2.url)
        print(response2.status_code)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)

    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()