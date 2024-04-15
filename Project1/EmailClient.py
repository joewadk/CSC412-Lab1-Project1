from socket import *
#zzoj ipci intn twat
mailserver= "smtp.google.com" #server host we will be using
serverPort=25 #port the socket uses (think of localhost:5000 when deploying a webapp)
message='HELO \r\n' #handshake message
dataCommand= 'DATA\r\n'

emailFrom= input('Enter your email address: ')
emailTo= input('Enter recipient email address: ')
emailFromCommand='MAIL FROM: <%s>\r\n' %emailFrom
emailToCommand='RCPT TO: <%s>\r\n' %emailTo

clientSocket = socket(AF_INET, SOCK_STREAM) #note we use STREAM instead of DGRAM for the socket type 
clientSocket.connect((mailserver,serverPort))
clientSocket.send(message.encode())
tcpResponse=clientSocket.recv(1024)
print(tcpResponse)
clientSocket.close()

clientSocket.send(emailFromCommand.encode())
clientSocket.send(emailToCommand.encode())
clientSocket.send(dataCommand.encode())

emailData= 'Subject: Comp Network Project 1 Test'