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


class DestrictsTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("行政区测试开始")

    def test_destricts_get(self):
        url = "http://recycling.3po-dwm.com:7777/api/districts"
        params = {
            "code": "350600",
            "subdistrict": 1
        }
        headers = {
            'accept': 'application/json'
        }
        response = requests.get(url, params=params, headers=headers)
        print(response.url)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)



    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()