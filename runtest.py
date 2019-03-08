# coding=utf-8
'''
Created on 2018-11-14
@author: kara
Project:漳州手持机测试用例
'''
import unittest
import os
import time
from test_case_backend import test_auth
from test_case_backend import test_employees1
from test_case_backend import test_vehicles
from test_case_backend import test_appversionmanagement
from test_case_backend import test_customers
from test_case_backend import test_collectionplans
from test_case_backend import test_collectionroutes
from  test_case_backend import test_collectiontask

from test_case_handsetadmin import test_auth1
from test_case_handsetadmin import test_RFID
from test_case_handsetadmin import test_customertypes
from test_case_handsetadmin import test_destricts
from test_case_handsetadmin import test_employees
from test_case_handsetadmin import test_vehicles1
from test_case_handsetadmin import test_customers1



import fileoperation







from HTMLTestRunner import HTMLTestRunner

# 报告存放路径
report_path = "/Users/kara/zhangzhou-interfacetest/report"
print(report_path)

#构造测试集
suite = unittest.TestSuite()
# 收运系统后端接口测试
'''suite.addTest(test_auth.AuthTest('test_auth_post'))
suite.addTest(test_auth.AuthTest('test_auth_get'))
suite.addTest(test_employees1.EmployeesTest('test_employees_post'))
suite.addTest(test_employees1.EmployeesTest('test_employees_put'))
suite.addTest(test_employees1.EmployeesTest('test_employees_delete'))
suite.addTest(test_employees1.EmployeesTest('test_employees_get'))
suite.addTest(test_vehicles.Vehicles_Test('test_vehicles_get'))
suite.addTest(test_vehicles.Vehicles_Test('test_vehicles_post'))
suite.addTest(test_vehicles.Vehicles_Test('test_vehicles_put'))
suite.addTest(test_vehicles.Vehicles_Test('test_vehicle_delete'))

suite.addTest(test_appversionmanagement.AppversionmanagementTest('test_appversionmanangement_post'))
suite.addTest(test_appversionmanagement.AppversionmanagementTest('test_appversionmanagement_get'))
suite.addTest(test_customers.CustomersTest('test_customers_get'))
suite.addTest(test_customers.CustomersTest('test_customers_post'))
suite.addTest(test_customers.CustomersTest('test_customers_put'))
suite.addTest(test_customers.CustomersTest('test_customers_separatepost'))
suite.addTest(test_customers.CustomersTest('test_customer_delete'))

suite.addTest(test_collectionplans.CollectionplansTest('test_collectionplans_get'))
suite.addTest(test_collectionplans.CollectionplansTest('test_collectionplans_post'))
suite.addTest(test_collectionplans.CollectionplansTest('test_collectionplans_routes_post'))
suite.addTest(test_collectionplans.CollectionplansTest('test_collectionplans_routesupdate_patch'))
suite.addTest(test_collectionplans.CollectionplansTest('test_collectionplans_operations_post'))
suite.addTest(test_collectionplans.CollectionplansTest('test_collectionplans_route_delete'))
suite.addTest(test_collectionplans.CollectionplansTest('test_collectionplans_plan_delete'))
suite.addTest(test_collectionroutes.CollectionroutesTest('test_collectionroutes_get'))
suite.addTest(test_collectionroutes.CollectionroutesTest('test_collectionroutes_task_post'))
suite.addTest(test_collectionroutes.CollectionroutesTest('test_collectionroutes_task_get'))
suite.addTest(test_collectionroutes.CollectionroutesTest('test_collectionroutes_task_priority_patch'))
suite.addTest(test_collectionroutes.CollectionroutesTest('test_collectionroutes_task_delete'))
suite.addTest(test_collectiontask.CollectiontaskTest('test_collectiontask_get'))
suite.addTest(test_collectiontask.CollectiontaskTest('test_collectiontask_post'))
suite.addTest(test_collectiontask.CollectiontaskTest('test_collectiontask_put'))
suite.addTest(test_collectiontask.CollectiontaskTest('test_collectiontask_delete'))'''



# 手持机管理端api测试
'''suite.addTest(test_auth1.Auth1Test('test_auth_post'))
suite.addTest(test_auth1.Auth1Test('test_auth_get'))
suite.addTest(test_customertypes.CustomertypesTest('test_customertype_get'))
suite.addTest(test_destricts.DestrictsTest('test_destricts_get'))'''
'''suite.addTest(test_RFID.RFIDTest('test_RFID_get'))'''
'''suite.addTest(test_employees.EmployeesTest('test_employees_get'))
suite.addTest(test_employees.EmployeesTest('test_employees_RFID_post'))
suite.addTest(test_employees.EmployeesTest('test_employees_RFID_delete'))
suite.addTest(test_vehicles1.VehiclesTest1('test_vehicles_get'))
suite.addTest(test_vehicles1.VehiclesTest1('test_vehicle_RFID_post'))
suite.addTest(test_vehicles1.VehiclesTest1('test_vehicle_RFID_delete'))'''
suite.addTest(test_customers1.CustomersTest1('test_customers_get'))
suite.addTest(test_customers1.CustomersTest1('test_customers_post'))
suite.addTest(test_customers1.CustomersTest1('test_customers_id_get'))
suite.addTest(test_customers1.CustomersTest1('test_customers_put'))
suite.addTest(test_customers1.CustomersTest1('test_customers_RFID_post'))
suite.addTest(test_customers1.CustomersTest1('test_customers_RFID_delete'))
suite.addTest(test_customers1.CustomersTest1('test_customers_uploadimages_post'))
suite.addTest(test_customers1.CustomersTest1('test_customers_delete'))






if __name__=='__main__':
   now = time.strftime("%Y-%m-%d-%H-%M-%S")
   report_abspath = os.path.join(report_path,"result_"+now+".html")
   fp = open(report_abspath,"wb")
   runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'接口自动化测试报告，测试结果如下：',description=u'用例执行情况：')
   runner.run(suite)
   fileoperation.send_email(report_abspath)
