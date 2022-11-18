#Importazione modulo socket dalla libreria standard
import socket

#Importiamo il modulo IP dalla libreria IPy Ip/Cornvertire l'hostname nel formato più corretto ip address
from IPy import IP


"""
La funzione scan prende in considerzione due parametri, target e numero delle porte
"""

def scan(target, portrange):
    lowport = int(portrange.split('-')[0])
    highport = int(portrange.split('-')[1])+ 1 
    # Il parametro target viene controllato dalla funzione check_ip per un'eventuale conversione da hostname ad ip
    converted_ip = check_ip(target)
    print('\n' + '[Scansione Target...] ' + str(target))
    for port in range(lowport, highport):
    	scan_port(converted_ip, port)


"""
La funzione get_banner riceve i dati dalle porte aperte  restituendoci il tipo di servizio aperto sulla porta.
"""

def get_banner(s):
    return s.recv(1024)


"""
La funzione check_ip con parametro "ip". Controlla l' inserimento corretto del target  nel formato dell'indirizzo IP, restituiendolo.
"""

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    # O convertendo  l'hostname nel formato dell'indirizzo IP corretto .
    except ValueError:
        return socket.gethostbyname(ip)


"""
La funzione scan_port tiene in considerazione i parametri  ipaddress e porta.
"""

def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        #Stabilisce la connessione con il target mandando una richiesta ad ogni porta ed analizzando la risposta
        sock.connect((ipaddress, port))
        try:
            #banner = get_banner(sock) --- Seguendo questa strada invece avremmo avuto servizi un po' più esplicativi
            banner = socket.getservbyport(port, "tcp")
            # Stampando i banner se presenti o restituendo solo risultato 'open' in caso contrario
            print('[+] Porta Aperta ' + str(port) + ' : ' + str(banner))
        except:
            print('[+] Porta Aperta ' + str(port))
    except:
        pass


#
# Di seguito l'esecuzione del programma NMAP
#


"""
Richiesta inserimento target tramite input()
"""

targets = input('[+] Inserire IP del\dei Target ( Dividi i target con una ,): ')
port_range = input('[+] Inserisci il RANGE di porte per lo SCAN ( Es. 1 - 4353 ): ')
lowport = int(port_range.split('-')[0])

# Controlliamo se sono inseriti più target in input
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '), port_range)
# O Scansioniamo target e porta singolarmente.
else:
    scan(targets, port_range)
