import socket
import random
import time

# Daftar kata warna dalam bahasa Inggris
colors_en = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown']

# Daftar terjemahan kata warna dalam bahasa Indonesia
color_translations = {
    'red': 'merah',
    'blue': 'biru',
    'green': 'hijau',
    'yellow': 'kuning',
    'orange': 'jingga',
    'purple': 'ungu',
    'brown' : 'coklat',
    'pink' : 'merah muda'
}

# Fungsi untuk mengirim pesan ke semua klien
def send_to_all_clients(sock, message, clients):
    for client_address in clients:
        sock.sendto(message.encode(), client_address)

# Fungsi untuk menerima pesan dari klien
def receive_from_client(sock):
    data, addr = sock.recvfrom(2104)
    return data.decode(), addr

# Fungsi utama
def main():
    # Inisialisasi socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Daftar klien yang terhubung
    clients = {}

    print("Server started.")

    while True:
        # Kirim kata warna acak ke semua klien setiap 10 detik
        color = random.choice(list(color_translations.keys()))
        send_to_all_clients(server_socket, color, list(clients.keys()))
        print("Sent color:", color)

        # Terima jawaban dari klien dalam waktu 10 detik
        server_socket.settimeout(10)
        try:
            response, client_address = receive_from_client(server_socket)
            response = response.lower()
            expected_translation = color_translations[color]
            if response == expected_translation:
                print("Correct answer from client", client_address)
                server_socket.sendto("100".encode(), client_address)
            else:
                print("Incorrect answer from client", client_address)
                server_socket.sendto("0".encode(), client_address)
        except socket.timeout:
            print("No response from clients")

        # Cek apakah ada klien baru yang ingin terhubung
        try:
            data, client_address = server_socket.recvfrom(1024)
            if client_address not in clients:
                clients[client_address] = True
                print("New client connected:", client_address)
        except socket.error:
            pass

        time.sleep(10)

if __name__ == "__main__":
    main()
