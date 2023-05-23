from socket import * #import modul socket 
import sys #import modul sys untuk terminate program
 
serverSocket = socket(AF_INET, SOCK_STREAM) #inisiasi socket sebagai objek
serverPort = 23489 #nomor port
serverAddress = "localhost" #server address sebagai alamat untuk mengakses website
serverSocket.bind((serverAddress, serverPort)) #menentukan IP address dan port yang digunakan dengan bind
serverSocket.listen(1) #socket dapat menerima koneksi sebanyak 1 koneksi pada satu waktu

#function untuk mengembalikan respone message
def getRespone(respone):
    if respone == 200:
        return "HTTP/1.1 200 OK\n"
    elif respone == 404:
        return "HTTP/1.1 404 Not Found"
    
print("--------------------------------------")
while True:
    print("          Ready To Serve ...\n--------------------------------------")
    connectionSocket, addr = serverSocket.accept()

    print("Request Accepted From.") 
    print("IP Address   : ", addr[0])
    print("Port         : ", addr[1], "\n")

    try:
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1]
        f = open(filename[1:], 'r')
        outputdata = f.read()
       
        print("File Found.")
        header = "HTTP/1.1 200 OK\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send("\r\n".encode())
        print("Respone      : ", getRespone(200))
        print("IP Address   : ", serverAddress)
        print("Port         : ", serverPort, "\n")

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        print("File Sent.")
        connectionSocket.close()

    except IOError:
        print("File Not Found.")

        Header = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(Header.encode())
        connectionSocket.send("\r\n".encode())

        print("Respone      : ", getRespone(404))

        f = open("404.html", 'r')
        outputdata = f.read()

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Terminates the connection
        connectionSocket.close()
        
    print("--------------------------------------")

serverSocket.close()
sys.exit()
