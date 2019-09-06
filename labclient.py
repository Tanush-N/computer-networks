from socket import *
serverport=12000
serverName='DESKTOP-4570CO1'
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverport))
file=input("enter file name")
clientSocket.send(file.encode())
modsent=clientSocket.recv(1024)
print("from server:",modsent.decode())
clientSocket.close()
