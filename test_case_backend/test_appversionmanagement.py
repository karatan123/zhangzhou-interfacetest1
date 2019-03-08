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
from urllib import request
from urllib import parse
from urllib.request import urlopen

token = ''

class AppversionmanagementTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("app管理测试开始")
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

    def test_appversionmanangement_post(self):
        global token
        values={}
        values['version'] = 3.3
        values['description'] = "测试数据"
        data = parse.urlencode(values).encode('utf-8')
        print(data)
        stringdata = data.decode()
        print(stringdata)

        url = "http://recycling.3po-dwm.com:8888/api/apps"+"?"+stringdata
        print(url)
        # 创建form data形式数据  主要是针对上传文件
        multipart_encoder = MultipartEncoder(
            fields={
                # 这里根据服务器需要的参数格式进行修改
                # "description": u"测试数据",
                # "version": 0.1,
                'apk': ('zhangZhouRecycling1.0_release.apk', open('/Users/kara/Desktop/zhangZhouRecycling1.0_release.apk', 'rb'), 'application/vnd.android.package-archive')
            },
            boundary='----WebKitFormBoundaryFsbnOAOXweGMsjT3'
        )

        headers = {
           'accept': '*/*',
           'Content-Type': "multipart/form-data; boundary=----WebKitFormBoundaryFsbnOAOXweGMsjT3",
           "Authorization": "Bearer " + token
        }
        response = requests.post(url, data=multipart_encoder, headers=headers)
        print(response.status_code)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_appversionmanagement_get(self):
        global token
        url = "http://recycling.3po-dwm.com:8888/api/apps/latest"
        headers = {
            'accept': '*/*',
            "Authorization": "Bearer " + token
        }
        response1 = requests.get(url, None, headers=headers)
        print(response1.status_code)
        print(response1.headers)
        print(response1.json())
        self.assertEqual(response1.status_code, 200)

    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()