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
postid1 = 0
class CollectionplansTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("后端方案管理测试开始")

    def test_collectionplans_get(self):
        url = "http://recycling.3po-dwm.com:8888/api/plans"
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

    def test_collectionplans_post(self):
        url = "http://recycling.3po-dwm.com:8888/api/plans"
        body = {
             "category": "Formal",
             "name": "新方案karatan"
         }
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
         }
        response1 = requests.post(url, '', json=body, headers=headers)
        print(response1.url)
        print(response1.status_code)
        print(response1.json())
        self.assertEqual(response1.status_code, 200)
        #     第三步：正则提取需要的参数值方案id
        global postid
        s = response1.json()
        postid = s["data"]["id"]
        print(postid)

    def test_collectionplans_routes_post(self):
        global postid
        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid) + "/routes"
        body = {
              "name": "线路1"
         }
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }
        response2 = requests.post(url, '', json=body, headers=headers)
        print(response2.url)
        print(response2.status_code)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)
        #     第三步：正则提取需要的参数值线路id
        global postid1
        s = response2.json()
        postid1 = s["data"]["id"]
        print(postid1)


    def test_collectionplans_routesupdate_patch(self):
        global postid
        global postid1
        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid) + "/routes/" + str(postid1)
        body = {
            "name": "线路1",
            "priority": 1,
            "vehicle": "闽Y12345"
         }
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }
        response3 = requests.patch(url, json=body, headers=headers)
        print(response3.url)
        print(response3.status_code)
        print(response3.json())
        self.assertEqual(response3.status_code, 200)

    def test_collectionplans_operations_post(self):
        global postid
        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid) + "/operations"
        data = {
            "event": "EXECUTE",
            "operate": "EXECUTE"
        }
        headers = {
            "accept": "*/*"
        }
        response4 = requests.post(url, data=data, json='', headers=headers)
        print(response4.url)
        print(response4.status_code)
        print(response4.json())
        self.assertEqual(response4.status_code, 200)

    def test_collectionplans_route_delete(self):
        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid) + "/routes/" + str(postid1)
        headers = {
            "accept": "*/*"
        }
        response5 = requests.delete(url, headers=headers)
        print(response5.url)
        print(response5.status_code)
        print(response5.json())
        self.assertEqual(response5.status_code, 200)

    def test_collectionplans_plan_delete(self):
        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid)
        headers = {
            "accept": "*/*"
        }
        response6 = requests.delete(url, headers=headers)
        print(response6.url)
        print(response6.status_code)
        print(response6.json())
        self.assertEqual(response6.status_code, 200)

    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()