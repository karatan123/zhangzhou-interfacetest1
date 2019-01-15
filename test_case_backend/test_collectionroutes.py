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

postid = 0
postid1 = 0
class CollectionroutesTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("收运线路管理测试开始")
    #     先创建个方案并创建线路
        url = "http://recycling.3po-dwm.com:8888/api/plans"
        body = {
            "category": "Formal",
            "name": "新方案karatan"
        }
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }
        response = requests.post(url, '', json=body, headers=headers)
        #     第三步：正则提取需要的参数值方案id
        global postid
        s = response.json()
        postid = s["data"]["id"]
        print(postid)
        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid) + "/routes"
        body = {
            "name": "线路1"
        }
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }
        response1 = requests.post(url, '', json=body, headers=headers)
        #     第三步：正则提取需要的参数值线路id
        global postid1
        s1 = response1.json()
        postid1 = s1["data"]["id"]
        print(postid1)

    def test_collectionroutes_get(self):
        global postid
        url = "http://recycling.3po-dwm.com:8888/api/routes"
        params = {
            "name": "线路1",
            "planId": postid
        }
        headers = {
            "accept": "*/*"
        }
        response2 = requests.get(url, params=params, headers=headers)
        print(response2.url)
        print(response2.status_code)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)

    def test_collectionroutes_task_post(self):
        url = "http://recycling.3po-dwm.com:8888/api/routes/" +str(postid1) + "/tasks"
        data = {
            "taskIds": "1"
        }
        headers = {
            "accept": "*/*"
        }
        response3 = requests.post(url, data=data, json='', headers=headers)
        print(response3.status_code)
        print(response3.json())
        self.assertEqual(response3.status_code, 200)

    def test_collectionroutes_task_get(self):
        global postid1
        url = "http://recycling.3po-dwm.com:8888/api/routes/" + str(postid1) + "/tasks"
        headers = {
            "accept": "*/*"
        }
        response3 = requests.get(url, '', headers=headers)
        print(response3.url)
        print(response3.status_code)
        print(response3.json())
        self.assertEqual(response3.status_code, 200)

    def test_collectionplans_task_priority_patch(self):
        global postid1
        url = "http://recycling.3po-dwm.com:8888/api/routes/" + str(postid1) + "/tasks"
        body = [
            {
             "id": 1,
             "priority": 1
            }
         ]
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }
        response4 = requests.patch(url, json=body, headers=headers)
        print(response4.url)
        print(response4.status_code)
        print(response4.json())
        self.assertEqual(response4.status_code, 200)

    def test_collectionplan_task_delete(self):
        global postid1
        values = {}
        values['taskIds'] = '1'
        data = parse.urlencode(values).encode('utf-8')
        print(data)
        stringdata = data.decode()
        print(stringdata)
        url = "http://recycling.3po-dwm.com:8888/api/routes/" + str(postid1) + "/tasks?taskIds=" +stringdata
        headers = {
            "accept": "*/*"
        }
        response5 = requests.delete(url, headers=headers)
        print(response5.url)
        print(response5.status_code)
        print(response5.json())
        self.assertEqual(response5.status_code, 200)

    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()