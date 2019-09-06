from socket import *
serverPort=12000
serverName='DESKTOP-4570CO1'
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while 1:
    connectionsocket,addr=serverSocket.accept()
    sentence=connectionsocket.recv(1024)
    file=open(sentence,"r")
    a=file.read(1024)
    #capitalizedsentence=sentence.upper()
    connectionsocket.send(a.encode())
    file.close()
    connectionsocket.close()
    
