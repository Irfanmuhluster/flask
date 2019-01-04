import socket
# intinya berkomunikasi dg 2 komputer/lebih
# bind = Method ini digunakan untuk menghubungkan alamat ip dengan
# nomor port ke
# socket. Socket harus dibuka dahulu sebelum terhubung dengan alamat tersebut.

# bind digunakan untuk menghubungkan socket dengan alamat server
# echo client = connect () untuk memasang socket langsung ke alamat remote
# intinya berbedaannya server mengunakan bind dan clien menggunakan connect
# berarti aku harus menentukan mana yg bertindak sbg client dan mana server?
# pertanyaannya.. bagaimana menentukan utk bind ke ip client?


class socket(object):
    server = socket.socket()
    server.bind(('192.168.12.53', 5889))  # ini alamat ip komputer
    server.listen(4)  # jumlah koneksi maksimum yg dpt ditangani server
    client_socket, client_address = server.accept()
    print(client_address, "has connected")
    while True:
        recvieved_data = client_socket.recv(1024)
        print(recvieved_data)
