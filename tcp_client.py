from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)
serverAddress = '127.0.0.1'
serverPort = 23489
filename = 'index.html'
server = (serverAddress, serverPort)
clientSocket.connect(server)

def get(server, filename):
    #clientSocket = socket(AF_INET, SOCK_STREAM)
    #clientSocket.connect(server)

    request = f'GET /{filename} HTTP/1.1\r\nHost: {serverAddress}:{serverPort}\r\n\r\n'
    clientSocket.send(request.encode())
    print("Request message sent.")

    # Recieving the response
    print("Server HTTP Response:\r\n")

    # This loop is necessary because we don't know if the entire message will be
    # recieved at the same recv() call. If there is a timeout and no new data has
    # arrived, we have the entire response.
    data = ""
    while True:
        clientSocket.settimeout(5)
        newData = clientSocket.recv(1024).decode()
        data += newData
        if len(newData) == 0:
            break
    print(data)

    clientSocket.close()

if __name__ == '__main__':
    get(server, filename)