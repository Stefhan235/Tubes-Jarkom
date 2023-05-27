from socket import * #import modul socket 
import sys #import modul sys untuk terminate program
 
serverSocket = socket(AF_INET, SOCK_STREAM) #inisiasi socket server sebagai objek, dengan 2 parameter yakni:
# 1. AF_INET: menunjukkan jaringan yg mendasari server ini adalah IPv4
# 2. SOCK_STREAM: artinya tipe socketnya TCP

serverPort = 23489 #nomor port
serverAddress = "localhost" #server address sebagai alamat untuk mengakses website
serverSocket.bind((serverAddress, serverPort)) #menentukan IP address dan port yang digunakan dengan bind
serverSocket.listen(1) #socket dapat menerima koneksi sebanyak 1 koneksi pada satu waktu

#function untuk mengembalikan respone message
def getRespone(respone): 
    if respone == 200: #jika respone bernilai 200 masuk if
        return "HTTP/1.1 200 OK\n" #return string "HTTP/1.1 200 OK\n"
    elif respone == 404: #jika respone bernilai 404 masuk elif
        return "HTTP/1.1 404 Not Found" #return string "HTTP/1.1 404 Not Found"
    
print("--------------------------------------")#print garis pemisah antara koneksi
while True: #loop selamanya 
    #menerima koneksi yang masuk
    print("          Ready To Serve ...\n--------------------------------------") #untuk print di sisi server bahwa server siap menerima
    connectionSocket, addr = serverSocket.accept() #membuat socket baru bernama connectionSocket untuk klien yang telah terkoneksi lalu addressnya klien ditaruh di addr

    try: #mencoba jalankan bagian kode ini dahulu, jika ada kesalahan masuk ke 'except'
        #menerima request dari klien
        message = connectionSocket.recv(2048).decode()#menerima pesan(request) dari klien dengan maksimum data sebesar 2048 byte serta diubah menjadi string
        filename = message.split()[1] #membagi pesan(request) klien dan diambil elemen kedua yang umumnya ditentukan sebagai path file yang diminta klien
        f = open(filename[1:], 'r') #membuka filename yang berisi path file yang diminta dimulai dari indeks kedua karena indeks pertama tidak diperlukan yaitu "/", lalu menggunakan mode "r" yaitu membaca file
        outputdata = f.read() #membaca isi file yang telah dibuka dan disimpan di 'outputdata'

        #print informasi klien yang connected
        print("Request Accepted From.") #print di server bahwa permintaan klien telah diterima oleh server
        print("IP Address   : ", addr[0]) #print alamat ip klien yang terconnect
        print("Port         : ", addr[1], "\n") #print nomor port yang digunakan klien
       
        #kirim pesan(balasan) ke klien
        print("File Found.") #print di server bahwa file yang diminta telah ditemukan
        header = "HTTP/1.1 200 OK\nContent-Type: text/html;\r\n\r\n" #header yang akan dikirim klien dalam format html dengan status 200 OK 
        connectionSocket.send(header.encode()) #mengirim pesan(balasan) setelah diubah menjadi byte 
        connectionSocket.send("\r\n".encode()) #mengirim baris kosong setelah diubah menjadi byte sebagai pemisah antara header dan isi file
        print("Respone      : ", getRespone(200)) #print ke server menunjukkan respon dari server memanggil fungsi 'getRespone()' dengan parameter 200
        print("IP Address   : ", serverAddress) #print alamat IP server
        print("Port         : ", serverPort, "\n") #print port server

        #kirim isi file ke klien
        for i in range(0, len(outputdata)): #iterasi sepanjang outputdata
            connectionSocket.send(outputdata[i].encode()) #mengirim setiap karakter dalam output data setelah diubah menjadi byte
        connectionSocket.send("\r\n".encode()) #mengirim baris kosong setelah mengirim isi file

        print("File Sent.") #print ke server menunjukan bahwa file telah dikirim ke klien
        connectionSocket.close()#terminasi koneksi

    except IOError: #dijalankan ketika ada error saat membuka file yang diminta klien
        #print informasi klien yang connected
        print("Request Accepted From.") #print di server bahwa permintaan klien telah diterima oleh server
        print("IP Address   : ", addr[0]) #print alamat ip klien yang terconnect
        print("Port         : ", addr[1], "\n") #print nomor port yang digunakan klien

        #kirim pesan(balasan) ke klien
        print("File Not Found.")  #print di server bahwa file yang diminta tidak ditemukan
        Header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html; \r\n\r\n" #header yang akan dikirim klien dalam format html dengan status 404 Not Found 
        connectionSocket.send(Header.encode()) #mengirim pesan(balasan) setelah diubah menjadi byte 
        connectionSocket.send("\r\n".encode())#mengirim baris kosong setelah diubah menjadi byte sebagai pemisah antara header dan isi file
        print("Respone      : ", getRespone(404)) #print ke server menunjukkan respon dari server memanggil fungsi 'getRespone()' dengan parameter 400

        # Kirim isi file 404.html ke klien
        f = open("404.html", 'r') #membuka 404.html yang berisi halaman untuk menampilkan pesan 404 Not Found
        outputdata = f.read() #membaca isi file yang telah dibuka dan disimpan di 'outputdata'

        #kirim isi file ke klien
        for i in range(0, len(outputdata)): #iterasi sepanjang outputdata
            connectionSocket.send(outputdata[i].encode()) #mengirim setiap karakter dalam output data setelah diubah menjadi byte
        connectionSocket.send("\r\n".encode()) #mengirim baris kosong setelah mengirim isi file

        
        connectionSocket.close() #terminasi koneksi
        
    print("--------------------------------------") #print garis pemisah antara koneksi

serverSocket.close() #terminasi server
sys.exit() #terminasi program
