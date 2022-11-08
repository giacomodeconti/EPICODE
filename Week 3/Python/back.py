import socket
SRV_ADDR=input('Type the server IP address: ')
SRV_PORT=input('Type the server port: ')
def print_menu():
    print('''\n\n0) Close the conntection
1) Get system info
2) List directory contenets''')
my_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect,str((SRV_ADDR, SRV_PORT))
print('Connection established')
print_menu()
while 1:
    message=input('\n-Select an option:')
    if message=='0':
        my_sock.sendall(message.encode())
        my_sock.close()
        break
    elif message=='1':
        my_sock.sendall(message.encode())
        data=my_sock.recv(1024)
        if not data: berak
        print(data.decode('utf-8'))
    elif message=='2':
        path=input('Insert the path: ')
        my_sock.sendall(message.encode())
        my_sock.sendall(path.encode())
        data=my_sock.recv(1024)
        data=data.decode('utf-8').split(',')
        print('*'*40)
        for x in data:
            print(x)
        print('*'*40)
