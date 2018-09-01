# ccxt_to_csv_to_mysql



用 pip install ccxt  获取 比特币各个交易所数据

使用到的python文件 ccxt_market_data.py


大致的思路

(备注:1,2 在国外vps上运行,linux,windows均可)

1.先安装 ccxt   pip install ccxt 

2.获取交易所比特币等数据 csv格式, 命令行模式下运行 python /root/ccxt_market_data2.py -s BTC/USDT -e binance -t 1m
获取到的文件 binance-BTCUSDT-1m.csv , 
Timestamp,Open,High,Low,Close,Volume
1535710500000,6972.0,6974.0,6971.02,6971.05,22.762053
1535710560000,6971.05,6974.0,6962.34,6966.21,43.335086
1535710620000,6966.25,6968.32,6960.0,6965.45,36.691563
1535710680000,6965.44,6972.65,6962.87,6965.96,49.018599
(注意 binance 用 ccxt_market_data2.py, okex 用ccxt_market_data.py,主要是okex不支持 limit=1000)

可以生产批处理文件, linux用 sh , windows 用bat,cmd

linux 利用 计划任务 每隔一段时间运行, windows 我使用 定时软件ontime


3.由于需要翻墙,上面 12都是在国外的vps上运行,  本地windows机器用 Bitvise SSH Client 把需要的csv get下来 (或许直接用ftp速度更快)

命令:
C:\BitviseSSHClient\sftpc.exe 用户名@远程主机ip地址 -pw=密码 -cmd="get *.csv O:\vps1\ -o"
例子: 
C:\BitviseSSHClient\sftpc.exe root@185.225.110.110 -pw=84uf!ueu -cmd="get *.csv O:\vps1\ -o"


4. 用python 导入到python, 先建立数据库,表, 然后导入到数据库


