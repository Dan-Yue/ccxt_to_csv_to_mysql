# _*_ coding:utf-8 _*_
#python27

import csv
import MySQLdb

#https://wwshen.gitbooks.io/omooc2py/content/0MOOC/CSVtoMYSQL.html

#连接数据库（参照MySQL Workbench中的设定）

db = MySQLdb.connect(host='IP地址',
                     user='数据库用户名', passwd='密码')
cur = db.cursor()

Generaldata = csv.reader(file('M://TEMP//binance-BTCUSDT-1m.csv'))



cur.execute('USE Stock')
#cur.execute('DROP TABLE IF EXISTS T1') #用于卸掉旧表
  #cur.execute('DROP TABLE IF EXISTS T1') #用于卸掉旧表
#cur.execute('''CREATE TABLE T1(Sub INTEGER NOT NULL,Gender INTEGER,Age FLOAT,Education INTEGER)''')


Generaldata = csv.reader(file('Y://vps1//binance-BTCUSDT-1m.csv'))


table_name = 'sh600000_noid'

#for row in Generaldata:
##去除第一行
for row in list(Generaldata)[1:]:

    print(row)
    print(table_name)
    #print('''INSERT ignore INTO `%s` (Timestamp,Open,High,Low,Close,Volume) VALUES(%s,%s,%s,%s,%s,%s)''',(table_name,row[0],row[1],row[2],row[3],row[4],row[5])))
    #cur.execute('''INSERT INTO sh600000 ('Timestamp','Open','High,'Low','Close','Volume') VALUES(%s,%s,%s,%s,%s,%s)''',(row))
    #cur.execute('''INSERT ignore INTO sh600000 (Timestamp,Open,High,Low,Close,Volume) VALUES(%s,%s,%s,%s,%s)''',(row))
    #cur.execute('''INSERT ignore INTO sh600000 (Timestamp,Open,High,Low,Close,Volume) VALUES(%s,%s,%s,%s,%s,%s)''', (row))
    cur.execute('''INSERT ignore INTO `%s` (Timestamp,Open,High,Low,Close,Volume) VALUES(%s,%s,%s,%s,%s,%s)''' % (table_name,row[0],row[1],row[2],row[3],row[4],row[5]))
    #    cur.execute('''INSERT ignore INTO sh600000_noid (Timestamp,Open,High,Low,Close,Volume) VALUES(%s,%s,%s,%s,%s,%s)''' % row[0],row[1],row[2],row[3],row[4],row[5])


db.commit()
