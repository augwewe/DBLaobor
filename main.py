# -*- coding: utf-8 -*-
# @Time    : 2023/1/14 14:17
# @Author  :augwewe
# @FileName: main.py
# @Software: PyCharm
from cavaMy import MongoDB
from cavaMy.SqliteManage import SqliteOperation
if __name__ == '__main__':
    mongodb=MongoDB("FirstDBTest","Test1")
    info1 = {
        'id': '5',
        'name': 'amy',
        'birth': 2,
        'sex': 'girl'
    }
    the_test=mongodb.insert(info1)
    # conditon={"birth":{"$gt":5}}
    # the_test=mongodb.delete_many(conditon)