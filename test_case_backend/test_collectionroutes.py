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
import pymysql

postid = 0
postid1 = 0
token = ''
employee_id = 0
postidtask = 0
class CollectionroutesTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("收运线路管理测试开始")
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

    #     获取登录用户id
        #     從數據庫中獲取該用戶的id
        global employee_id
        db = pymysql.Connect(host='mysql-cn-south-1-36f43c39281c45a4.public.jcloud.com', port=3306,
                             user='recycling_root', passwd='Recycling2018', db='recycling_testing', charset='UTF8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "SELECT* FROM EMPLOYEES WHERE USERNAME='zhangzhou6605'"
        try:
            cursor.execute(sql)
            print(sql)
            result = cursor.fetchone()
            employee_id = result[0]
            print(employee_id)
        except:
            print("Error:unable to fatch data")

        # 关闭数据库连接
        db.close()

    #     先创建个方案并创建线路
        # 獲取當前時間
        timecurrent = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        planname = "新方案karatan" + str(timecurrent)
        print(planname)
        url = "http://recycling.3po-dwm.com:8888/api/plans"
        body = {
            "category": "Formal",
            "name": planname
        }
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        response = requests.post(url, '', json=body, headers=headers)
        #     第三步：正则提取需要的参数值方案id
        global postid
        s = response.json()
        postid = s["data"]["id"]
        print(postid)

        # 先锁定方案
        # 先鎖定對應方案及手動在數據庫中將方案的編輯人id寫入
        db = pymysql.Connect(host='mysql-cn-south-1-36f43c39281c45a4.public.jcloud.com', port=3306,
                             user='recycling_root', passwd='Recycling2018', db='recycling_testing', charset='UTF8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        sql = "SELECT* FROM COLLECTION_PLANS WHERE ID=%d" % (postid)
        try:
            cursor.execute(sql)
            print(sql)
            result = cursor.fetchone()
            user_id = result[8]
            print(user_id)
        except:
            print("Error:unable to fatch data")

        sql = "UPDATE COLLECTION_PLANS SET EDIT_USER_ID = %d WHERE ID = %d" % (employee_id, postid)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        # 关闭数据库连接
        db.close()

        time.sleep(10)

        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid) + "/routes"
        body = {
            "name": "线路1"
        }
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        response1 = requests.post(url, '', json=body, headers=headers)
        print(response1.url)
        print(response1.status_code)
        print(response1.json())
        #     第三步：正则提取需要的参数值线路id
        global postid1
        s1 = response1.json()
        postid1 = s1["data"]["id"]
        print(postid1)

    def test_collectionroutes_get(self):
        global postid
        global token
        url = "http://recycling.3po-dwm.com:8888/api/routes"
        params = {
            "name": "线路1",
            "planId": postid
        }
        headers = {
            "accept": "*/*",
            "Authorization": "Bearer " + token
        }
        response2 = requests.get(url, params=params, headers=headers)
        print(response2.url)
        print(response2.status_code)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)

    def test_collectionroutes_task_post(self):
        global token
        global postid1
        #首先得创建收运请求
        # 添加收運請求
        url = "http://125.94.39.168:8888/api/tasks"
        body = [
            {
                "amountOfGarbage": 2.5,
                "collectionPeriodId": 234,
                "customerId": 201350,
                "name": "小食堂",
                "taskList": [
                    {
                        "amountOfGarbage": 2.5,
                        "customerId": 201350,
                        "name": "小食堂"
                    }
                ]
            },
            {
                "amountOfGarbage": 2.5,
                "collectionPeriodId": 224,
                "customerId": 2,
                "name": "万科广场",
                "taskList": [
                    {
                        "amountOfGarbage": 1,
                        "customerId": 3,
                        "name": "万科广场-单位1"
                    },
                    {
                        "amountOfGarbage": 1.5,
                        "customerId": 4,
                        "name": "万科广场哈哈哈"
                    }
                ]
            }
        ]
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        response0 = requests.post(url, data='', json=body, headers=headers)
        print(response0.url)
        print(response0.status_code)
        print(response0.json())
        # 獲取收運請求id
        global postidtask
        s = response0.json()
        postidtask = s["data"][0]["id"]
        print(postidtask)

        url = "http://recycling.3po-dwm.com:8888/api/routes/" +str(postid1) + "/tasks"
        data = {
            "taskIds": postidtask
        }
        headers = {
            "accept": "*/*",
            "Authorization": "Bearer " + token
        }
        response3 = requests.post(url, data=data, json='', headers=headers)
        print(response3.url)
        print(response3.status_code)
        print(response3.json())
        self.assertEqual(response3.status_code, 200)

    def test_collectionroutes_task_get(self):
        global postid1
        global token
        url = "http://recycling.3po-dwm.com:8888/api/routes/" + str(postid1) + "/tasks"
        headers = {
            "accept": "*/*",
            "Authorization": "Bearer " + token
        }
        response3 = requests.get(url, '', headers=headers)
        print(response3.url)
        print(response3.status_code)
        print(response3.json())
        self.assertEqual(response3.status_code, 200)

    def test_collectionroutes_task_priority_patch(self):
        global postid1
        global token
        global postidtask
        url = "http://recycling.3po-dwm.com:8888/api/routes/" + str(postid1) + "/tasks"
        body = [
            {
             "id": postidtask,
             "priority": 2
            }
         ]
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        response4 = requests.patch(url, json=body, headers=headers)
        print(response4.url)
        print(response4.status_code)
        print(response4.text)
        self.assertEqual(response4.status_code, 200)


    def test_collectionroutes_task_delete(self):
        global postid1
        global token
        global postidtask
        global postid
        values = {}
        values['taskIds'] = postidtask
        data = parse.urlencode(values).encode('utf-8')
        print(data)
        stringdata = data.decode()
        print(stringdata)
        url = "http://recycling.3po-dwm.com:8888/api/routes/" + str(postid1) + "/tasks?" +stringdata
        headers = {
            "accept": "*/*",
            "Authorization": "Bearer " + token
        }
        response5 = requests.delete(url, headers=headers)
        print(response5.url)
        print(response5.status_code)
        print(response5.text)
        self.assertEqual(response5.status_code, 200)
    #     解锁方案
        # 解鎖方案  介紹方案后才能刪
        db = pymysql.Connect(host='mysql-cn-south-1-36f43c39281c45a4.public.jcloud.com', port=3306,
                             user='recycling_root', passwd='Recycling2018', db='recycling_testing', charset='UTF8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "UPDATE COLLECTION_PLANS SET EDIT_USER_ID= Null  WHERE ID = %d" % (postid)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

            # 关闭数据库连接
        db.close()

    @classmethod
    def tearDownClass(self):
            print(u"自动测试完毕！")

# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()