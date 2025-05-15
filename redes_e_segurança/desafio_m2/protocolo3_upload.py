from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login('dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')

filename = 'protocolo3exemplo.txt'

with open(filename, 'rb') as file:
    ftp.storbinary(f'STOR {filename}', file)

print(f"Arquivo '{filename}' enviado com sucesso!")
ftp.quit()