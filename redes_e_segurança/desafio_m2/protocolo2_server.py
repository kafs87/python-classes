import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12346))
server_socket.listen(1)

print("Servidor aguardando conexão...")

conn, addr = server_socket.accept()
print("Conectado por", addr)

dados = conn.recv(1024)
print("Mensagem recebida:", dados.decode())

conn.sendall(b"Mensagem recebida com sucesso!")
conn.close()
