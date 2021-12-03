import socket
import pyfiglet
from datetime import datetime
import sys
import nmap
from getmac import get_mac_address

banner = pyfiglet.figlet_format("Port Scanner")
print(banner)

linea = ("-------------------------------------------------------")
linea2 = ("-------------------------------------------------------")

hora = datetime.now()

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
escoje = int(input("Choose option \n 1- See status of one port  \n 2- See status of all ports \n 3- See status of range \n 4- Host Discovery \n Option: "))
host = input("Which host do you want to scan?\n Host: ")
all_ports = 1

def service(port):
    serv = socket.getservbyport(port)
    print(serv)


def un_puerto(port):
    port2 = 43
    print(linea)
    print(linea)
    print("Starting Scan...", hora)
    print(linea)
    print(linea,"\n")

    if socket1.connect_ex((host,port)):
        print("Closed")
    else:
        print("The Port", port, "are Opened")
        print("The service working are")
        service(port)

def todos(all_ports):
    try:
        for port in range(1,65535):  
            socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection = socket2.connect_ex((host, port))
            if connection == 0:
                serv = socket.getservbyport(port)
                print("Port", port,	 "are Opened \t", serv, "service working")
            socket2.close()

    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

def rango():
    try:
        for port in range(a,b):  
            socket4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection = socket4.connect_ex((host, port))
            if connection == 0:
                serv = socket.getservbyport(port)
                print("Port", port,	 "are Opened \t", serv, "service working")
            socket4.close()

    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()


def mac(IP="idk"):
    mac2 = get_mac_address(ip=IP)
    print(mac2)

def host_discover():
    a = nmap.PortScanner()
    print(linea2)
    print("Starting Scan...",hora)
    print(linea2)
    a.scan(hosts=hosts1, arguments="-sn")
    lista_hosts = [(x, a[x] ["status"]["state"]) for x in a.all_hosts()]
    print("Active hosts: \t   Status: \n")
    for host, status in lista_hosts:
        print("MAC:")
        print("IP:\n",host,"\t   ", status," ",mac(host),"\n")      

if escoje == 1:
    port = int(input("What port do you want to see the status of? \n Port: "))
    un_puerto(port)
elif escoje == 2:
    todos(all_ports)
elif escoje == 3:
    a = int(input("First number of range: "))
    b = int(input("Second number of range: "))
    rango()
elif escoje == 4:
    hosts1 = input("Your subnet (with CIDR x.x.x.x/CIDR) \n Subnet: ")
    host_discover()
else:
    print("Invalid option")


