import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

print("Servidor aguardando mensagens...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Mensagem recebida de {addr}: {data.decode()}")
    server_socket.sendto(b"Recebido!", addr)
