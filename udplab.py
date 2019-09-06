from socket import *
serverPort=25000
serverName='10.124.7.93'
clientSocket=socket(AF_INET,SOCK_DGRAM)
#clientSocket.connect((serverName,serverport))
file=input("enter file name")
clientSocket.sendto(file.encode(),(serverName,serverPort))
#clientSocket.send(sent.encode())
modsent,serverAddress=clientSocket.recvfrom(2048)
print("from server:",modsent.decode())
clientSocket.close()
