import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12346))

client_socket.sendall("Olá, servidor!".encode())

resposta = client_socket.recv(1024)
print("Resposta do servidor:", resposta.decode())

client_socket.close()
