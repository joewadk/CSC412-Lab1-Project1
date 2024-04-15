from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))
print('The server is ready to receive')
sequenceNum=0


while True:
    try:
        if(sequenceNum>=10):
            print('~~~~~~~~~~~~~Await New Ping Iteration~~~~~~~~~~~~~~')
            sequenceNum=0
        else:
            sequenceNum+=1
            backMessage= 'Pong#' + str(sequenceNum)
            message, clientAddress = serverSocket.recvfrom(1024)
            print('We have received sequence #%i' %sequenceNum)
            
            serverSocket.sendto(backMessage.encode(), clientAddress)
    except:
        pass