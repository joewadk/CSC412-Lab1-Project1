from socket import *
from datetime import datetime

serverPort=5000 #port the socket uses (think of localhost:5000 when deploying a webapp)
message='Ping'
pingPong={}

def sendPing():
        try: #exception handling for weird cases, will be scanned 
            clientSocket = socket(AF_INET, SOCK_DGRAM)
            time_sent= (datetime.now().microsecond)/1000 #grab current time in us, converts micro to milli 
            clientSocket.sendto(message.encode(),("localhost", serverPort)) #send the ping
            newMessage, clientAddress = clientSocket.recvfrom(1024)#await for pong
            newMessage_list=newMessage.decode().split('#') # decodes the message and initiates a list to get the pair 'pong',sequenceNum
            sequenceNum=int(newMessage_list[1]) #typecast the string sequenceNum into a int
            time_received= (datetime.now().microsecond)/1000 
            time_diff=time_received-time_sent #calculate rtt
            pingPong.update({sequenceNum:time_diff}) #add to the dictionary 
            clientSocket.close() #close the socket, pretty self-explanatory
        except:
             pass #if theres a weird case we skip, will check null values later 

            

def scan_errors():
    for i in pingPong.keys(): #iterate through all keys, ie all sequence numbers
         if (pingPong[i]==error or 'ERROR' or None) or pingPong[10]== None:  #we check if any of the values has an error or there is no tenth RTT to print
                clientSocket = socket(AF_INET, SOCK_DGRAM) #if we get an error, this will send another ping for this sequence
                time_sent= (datetime.now().microsecond)/1000 #grab current time in us, converts micro to milli 
                clientSocket.sendto(message.encode(),("localhost", serverPort)) #send the ping
                newMessage, clientAddress = clientSocket.recvfrom(1024)#await for pong
                time_received= (datetime.now().microsecond)/1000 
                time_diff=time_received-time_sent #calculate rtt
                pingPong.update({i:time_diff}) #add to the dictionary but this time at the i'th position

#just some logic functions for the print later on                
def values_mean(): #average
    sum=0.0
    count=0
    for i in pingPong.values():
        sum+=i
        count+=1
    return sum/count
def values_large(): #max
    max=0.0
    for i in pingPong.values():
        if i>max:
            max=i
    return max
def values_small(): #min
    min=pingPong[1]
    for i in pingPong.values():
        if i<min:
            min=i
    return min


for i in range(10): #send 10 pings
    sendPing() #call func
    scan_errors()


print('The mean RTT was: %f ms' %values_mean())
print('The longest RTT was: %f ms' %values_large())
print('The shortest RTT was: %f ms' %values_small())
