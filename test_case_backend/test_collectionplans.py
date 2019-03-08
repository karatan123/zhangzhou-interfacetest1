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


import pymysql
import os

postid = 0
postid1 = 0
token = ''
employee_id = 0
postidtask = 0
class CollectionplansTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("后端方案管理测试开始")
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

    def test_collectionplans_get(self):
        global token
        url = "http://recycling.3po-dwm.com:8888/api/plans"
        params = {
            "page": 1,
            "size": 20
        }
        headers = {
            "accept": "*/*",
            "Authorization": "Bearer " + token
        }
        response = requests.get(url, params=params, headers=headers)
        print(response.url)
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_collectionplans_post(self):
        global token
        # 獲取當前時間
        timecurrent = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        planname =  "新方案karatan" + str(timecurrent)
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
        global token
        global postid
        global employee_id

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
        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid) + "/routes"
        body = {
              "name": "线路1"
         }
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
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
        global token
        global postid
        global postid1
        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid) + "/routes/" + str(postid1)
        body = {
            "name": "线路1",
            "priority": 1,
            "vehicle": "闽Y88888"
         }
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        response3 = requests.patch(url, json=body, headers=headers)
        print(response3.url)
        print(response3.status_code)
        print(response3.json())
        self.assertEqual(response3.status_code, 200)

    # 沒有保存  或者無任務不讓執行任務
    def test_collectionplans_operations_post(self):
        global token
        global postid
        global postid1
        # 先添加收運請求，然後給線路添加收運任務
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

        # 給線路添加任務
        url = "http://125.94.39.168:8888/api/routes/" + str(postid1) + "/tasks"
        data = {
            "taskIds": postidtask
        }
        headers = {
            "accept": "*/*",
            "Authorization": "Bearer " + token
        }
        response0 = requests.post(url, data=data, json='', headers=headers)
        print(response0.url)
        print(response0.status_code)
        print(response0.json())

        # 保存方案后才能執行，即解鎖
        # 解鎖線路
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

        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid) + "/operations"
        data = {
            "event": "EXECUTE",
            "operate": "EXECUTE"
        }
        headers = {
            "accept": "*/*",
            "Authorization": "Bearer " + token
        }
        response4 = requests.post(url, data=data, json='', headers=headers)
        print(response4.url)
        print(response4.status_code)
        print(response4.json())
        self.assertEqual(response4.status_code, 200)

    def test_collectionplans_route_delete(self):
        global token
        global postid
        global postid1
        global employee_id
        # 鎖定方案
        db = pymysql.Connect(host='mysql-cn-south-1-36f43c39281c45a4.public.jcloud.com', port=3306,
                             user='recycling_root', passwd='Recycling2018', db='recycling_testing', charset='UTF8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        sql = "UPDATE COLLECTION_PLANS SET EDIT_USER_ID = %d WHERE ID = %d" % (employee_id, postid)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        # 关闭数据库连接
        db.close()
        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(postid) + "/routes/" + str(postid1)
        headers = {
            "accept": "*/*",
            "Authorization": "Bearer " + token
        }
        response5 = requests.delete(url, headers=headers)
        print(response5.url)
        print(response5.status_code)
        print(response5.json())
        self.assertEqual(response5.status_code, 200)

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



    def test_collectionplans_plan_delete(self):
        global token
        # 因为之前创建方案已执行  无法删除   现在先新建方案，来测试删除接口
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
        response1 = requests.post(url, '', json=body, headers=headers)
        print(response1.url)
        print(response1.status_code)
        print(response1.json())
        self.assertEqual(response1.status_code, 200)
        #     第三步：正则提取需要的参数值方案id
        s = response1.json()
        planid = s["data"]["id"]
        print(planid)

        url = "http://recycling.3po-dwm.com:8888/api/plans/" + str(planid)
        headers = {
            "accept": "*/*",
            "Authorization": "Bearer " + token
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