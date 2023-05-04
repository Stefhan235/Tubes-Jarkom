# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
# Fill in end
serverPort = 80
serverSocket.bind(("", serverPort))
serverSocket.listen(1)


def getRespone(respone):
    if respone == "200":
        return "HTTP/1.1 200 OK"
    elif respone == "404":
        return "HTTP/1.1 404 Not Found"


while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()  # Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024).decode()  # Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Fill in start #Fill in end
        # Send one HTTP header line into socket
        header = "HTTP/1.1 200 OK\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        respone = header.split()[1]
        print(getRespone(respone))
        print(outputdata)
        # Fill in start
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send a 404 Not Found HTTP response message to the client
        header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        respone = header.split()[1]
        print(getRespone(respone))
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())

        # Close the client connection socket
        connectionSocket.close()
    # Send response message forfile not found
    # Fill in start
    # Fill in end
    # Close client socket
    # Fill in start
    # Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding
data
