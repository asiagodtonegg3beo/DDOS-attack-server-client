import subprocess
import time

attack_ip=""
proto = ""
ports = []
TCP=[]
UDP=[]

def nmap_scan(attack_ip):
    try:
        proc = subprocess.Popen(["nmap","-T4","-F","-oG","t.txt",attack_ip], stdout=subprocess.PIPE, shell=True)
        proc.wait()
        print('scan done')
    except:
        print('error')

def port_analize():
    f = open("t.txt","r",encoding="utf-8")
    line = f.readlines()
    f.close()
    ports = line[2].split('Ports:')[1].split(',')
    #print(ports)

#print(ports[0].split('/')[2])
    for i in range(0,len(ports)):
        proto = ports[i].split('/')[2]
        if (proto=='tcp' or proto=='udp'):
            TCP.append(ports[i].split('/')[0])
    return TCP
'''
print(TCP)
print(UDP)

while True:
    for i in range(0,len(TCP)):
        print(TCP[i])
        #//attack here
'''
#print(protocol)
#nmap_scan()
#TCP = port_analize()

#print(TCP)

#(out, err) = proc.communicate()


#print('out:',out)
