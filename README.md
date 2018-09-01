# ccxt_to_csv_to_mysql


#功能: 数字货币k线数据导入到本地数据库mysql落地方案


用 ccxt (https://github.com/ccxt/ccxt) 获取 比特币各个交易所数据 (更多介绍看参考文档)


使用到的python文件 ccxt_market_data.py


大致的思路

翻墙服务器->安装pip install ccxt(python) ->用ccxt_market_data.py 下载各交易所数字货币csv-> 本地服务器远程从翻墙服务器获取文件-> 导入mysql数据库 -->用python pandas 从数据库导出文件,然后量化分析


(备注:1,2 在国外vps上运行,linux,windows均可)

1.先安装 ccxt   pip install ccxt 

2.获取交易所比特币等数据 csv格式, 命令行模式下运行 python /root/ccxt_market_data2.py -s BTC/USDT -e binance -t 1m

可以用批处理文件, linux用 sh , windows 用bat,cmd

获取到的文件 binance-BTCUSDT-1m.csv 

Timestamp,Open,High,Low,Close,Volume

1535710500000,6972.0,6974.0,6971.02,6971.05,22.762053

1535710560000,6971.05,6974.0,6962.34,6966.21,43.335086

1535710620000,6966.25,6968.32,6960.0,6965.45,36.691563

1535710680000,6965.44,6972.65,6962.87,6965.96,49.018599

(注意 binance 用 ccxt_market_data2.py, okex 用ccxt_market_data.py,主要是okex不支持 limit=1000)


linux 利用 计划任务 每隔一段时间运行sh, windows 我使用 定时软件ontime  bat或cmd批处理文件


3.由于需要翻墙,上面 12都是在国外的vps上运行,  本地windows机器用 Bitvise SSH Client 把需要的csv get下来 (或许直接用ftp速度更快)

命令:

C:\BitviseSSHClient\sftpc.exe 用户名@远程主机ip地址 -pw=密码 -cmd="get *.csv O:\vps1\ -o"

例子: 

C:\BitviseSSHClient\sftpc.exe root@185.225.110.110 -pw=84uf!ueu -cmd="get *.csv O:\vps1\ -o"


4. 用python 把下载下来的csv 导入到本地mysql, 先建立数据库,表, 然后导入到数据库
方法见 v1



参考文档

-----ccxt -----

python异步加协程获取比特币市场信息 https://www.cnblogs.com/xiaxuexiaoab/p/8410682.html

Demo to download hundreds of crypto currency pairs via CCXT Python package from Binance Bitmex OKEx exchanges
https://quantlabs.net/blog/2018/05/demo-download-hundreds-crypto-currency-pairs-via-ccxt-python-package-binance-bitmex-okex/
https://www.youtube.com/watch?v=Mf76ZVKsX8I

Easy Python script to download crypto currency market data with CCXT package
https://quantlabs.net/blog/2018/05/easy-python-script-to-download-crypto-currency-market-data-with-ccxt-package/
https://www.youtube.com/watch?v=PTGkJsrF7kQ

----mysql----
mysql-workbench 数据库管理
Navicat for MySQL 数据库管理



#其他帮助

python2.7.13安装MySQLdb模块及使用
命令行安装
    pip install python-mysql
    
或者
访问: http://www.lfd.uci.edu/~gohlke/pythonlibs/，

下载MySQL_python-1.2.5-cp27-none-win_amd64.whl   

注意这里了64版本,如果你安装的python是27 32版本请 MySQL_python‑1.2.5‑cp27‑none‑win32.whl

然后切换路径到 c:\py27\scripts\pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl 

网络帮助:https://blog.csdn.net/svap1/article/details/73684154






