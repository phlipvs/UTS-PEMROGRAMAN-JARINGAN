import socket

# Fungsi untuk menerima pesan dari server
def receive_from_server(sock):
    data, _ = sock.recvfrom(2104)
    return data.decode()

# Fungsi untuk mengirim jawaban ke server
def send_response_to_server(sock, response):
    sock.sendto(response.encode(), server_address)

# Inisialisasi socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Alamat server
server_address = ('localhost', 12345)

try:
    # Sambungkan ke server
    client_socket.sendto(b"connect", server_address)

    score = 0

    while True:
        # Terima kata warna dari server
        color = receive_from_server(client_socket)
        print("Received color:", color)

        # Beri jawaban
        response = input("Enter the color in B. Indonesia: ").lower().strip()

        # Kirim jawaban ke server
        send_response_to_server(client_socket, response)

        # Terima feedback dari server
        feedback = receive_from_server(client_socket)
        if feedback == "100":
            score = 100  # 100 ke skor jika jawaban benar
            print("Correct! Score: ", score)
        else:
            score = 0
            print("Incorrect!, Score: ", score)

except KeyboardInterrupt:
    print("Closing client...")
finally:
    client_socket.close()
