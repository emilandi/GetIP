
import socket
from os import system
from requests import get

system("cls")

#consulta IP local y nombre host
def getIP(): 
    try: 
        host = socket.gethostname() 
        ip = socket.gethostbyname(host)       
        print("Hostname :  ",host) 
        print("Local IP : ",ip)
    except: 
        print("error no se puede resolver la consulta")   

getIP()

#IP Publica
public = get('https://api.ipify.org').text
print ('Public IP Address: ' +  public)