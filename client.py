from socket import * #import modul socket
import sys #import modul sys untuk terminate program

clientSocket = socket(AF_INET, SOCK_STREAM) #inisiasi socket sebagai objek
# 1. AF_INET: menunjukkan jaringan yg mendasari server ini adalah IPv4
# 2. SOCK_STREAM: artinya tipe socketnya TCP

serverAddress = '127.0.0.1' #alamat server
serverPort = 23489 #nomor port
filename = input("Nama File yang Dicari : ") #input nama file yang akan di request ke server
server = (serverAddress, serverPort) # server ip dan port dijadiin tupel dimasukkan ke server
clientSocket.connect(server) #mencari koneksi ke server dengan alamat dan port yang telah ditentukan

# fungsi mengirim request dan menerima respons dari server
def get(server, filename):
    #send pesan(request)
    request = 'GET /' + filename + ' HTTP/1.1\r\nHost: ' + serverAddress + ':' + str(serverPort) + '\r\n\r\n' #membuat string 'request' berisi path file, versi protokol, dan header berisi alamat server dan port
    clientSocket.send(request.encode()) #mengirim pesan(request) ke server yang telah diubah menjadi byte
    print("Request message sent.") #print pesan bahwa pesan(request) telah dikirim

    # Recieving the response
    print("Server HTTP Response:\r\n")
    
    #membuat loop dimana menerima data sampai tidak ada data baru yang datang lalu masuk timeout dan keluar loop
    #ini dilakukan karena seluruh pesan belum tentu diterima di recv() yang sama
    data = "" #variable 'data' untuk menyimpan seluruh pesan respon server
    while True: #loop selamanya
        clientSocket.settimeout(5) #clientSocket di set timeout 5 detik, jika tidak ada data baru yang datang maka berhenti recv
        newData = clientSocket.recv(1024).decode() #menerima data dari server sebesar 1024 byte dan diubah menjadi string
        data += newData #menyimpan data yang baru diterima di 'data'
        if len(newData) == 0: #break jika panjang 'newData' == 0
            break
    print(data) #print seluruh respons dari server yang telah diterima

    clientSocket.close() #menutup koneksi socket

if __name__ == '__main__': #program main
    get(server, filename) #panggil procedure get
