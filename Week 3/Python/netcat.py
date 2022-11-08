import socket
SRV_ADDR='192.168.1.6'
SRV_PORT=4444
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print('conn wait...')
connection, addres=s.accept()
print('connected to ', addres)
while 1:
    data=connection.recv(1024)
    if not data: break
    print(data.decode('utf-8'))
connection.close()

