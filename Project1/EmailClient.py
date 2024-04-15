from socket import *

mailserver= "smtp.google.com"
serverPort=25 #port the socket uses (think of localhost:5000 when deploying a webapp)
message='HELO \r\n'
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,serverPort))
clientSocket.send(message.encode())
tcpResponse=clientSocket.recvfrom(1024)
print(tcpResponse)
clientSocket.close()