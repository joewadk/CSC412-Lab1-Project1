from socket import *
from datetime import datetime

time_sent= datetime.now().microsecond
serverName= '71.183.96.147'
serverPort=12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message= 'test\n'
clientSocket.sendto(message.encode(),(serverName, serverPort))
clientSocket.close()