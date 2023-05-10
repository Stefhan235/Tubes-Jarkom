from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 80
serverAddress = "localhost"
serverSocket.bind((serverAddress, serverPort))
serverSocket.listen(1)


def getRespone(respone):
    if respone == 200:
        return "HTTP/1.1 200 OK\n"
    elif respone == 404:
        return "HTTP/1.1 404 Not Found\n"


while True:
    print("Ready to serve...\n----------------------")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(2048).decode()

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
       

        header = "HTTP/1.1 200 OK\nContent-Type: text/html\r\n\r\n"
        print("Respone : ", getRespone(200))
        connectionSocket.send(header.encode())
        print("File Data : \n\n", outputdata, "\n")

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        print("Respone : ", getRespone(404))
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
        connectionSocket.close()

    print("----------------------")

serverSocket.close()
sys.exit()
