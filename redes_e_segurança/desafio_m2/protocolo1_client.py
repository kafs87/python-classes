import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Olá, servidor!"
client_socket.sendto(msg.encode(), ('localhost', 12345))

resposta, _ = client_socket.recvfrom(1024)
print("Resposta do servidor:", resposta.decode())