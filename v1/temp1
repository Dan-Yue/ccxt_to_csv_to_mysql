# _*_ coding:utf-8 _*_


#下一步 1.csv导入mysql_1.py


# 预测者 数据 导入数据库

# 生成唯一日期 避免重复

from sqlalchemy import create_engine
import MySQLdb
import pandas as pd

import tushare as ts

from pandas import Series, DataFrame

import numpy as np
import os

from datetime import datetime
from datetime import *
import time

pd.set_option('display.width', 200)


#engine = create_engine('mysql://root:password@ip/stock?charset=utf8')
conn = MySQLdb.connect(host='ip', user='root', passwd='password', charset="utf8")

# 股票代码
codenameall = [
    'sh600000_noid']

# 循环导入上述股票

for cdname in codenameall:

    acdname1 = cdname

    cursor = conn.cursor()
    conn.select_db('stock')

    #Timestamp,Open,High,Low,Close,Volume

#`id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,


    try:
        cursor.execute("""
          CREATE TABLE IF NOT EXISTS `%s`(
              `Timestamp` double NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
              `Open` double DEFAULT NULL,
              `High` double DEFAULT NULL,
              `Low` double DEFAULT NULL,
              `Close` double DEFAULT NULL,
              `Volume` double DEFAULT NULL

          ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
          """ % acdname1)






        cursor.close()
        print "sql ok"
    except:
        cursor.close()
        print "sql not ok, already exists"



'''
# 设置主键唯一
cursor.execute("""
      ALTER TABLE `%s` ADD PRIMARY KEY(id);
      """ % acdname1)



# 设置索引唯一
cursor.execute("""
  ALTER TABLE `%s` ADD UNIQUE(`Timestamp`);
  """ % acdname1)


'''
