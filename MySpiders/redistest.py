#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import pickle
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DBOps.settings")
import django
django.setup()
from DBOps.db.models import *


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1


r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
# r.set('name', 'junxi')  # key是"foo" value是"bar" 将键值对存入redis缓存
# print(r['name'])
# print(r.get('name'))  # 取出键name对应的值
# print(type(r.get('name')))
# obj=Employee(name='Jack',salary=200)
# pickled_object = pickle.dumps(obj)
# r.set('Jack', pickled_object)

unpacked_object = pickle.loads(r.get('20191209'))
print ''