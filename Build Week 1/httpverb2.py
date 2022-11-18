import http.client #modulo che definisce le classi che implementano il lato client del protocollo HTTP

host = input("Inserire host/IP del sistema target: ") #variabile per l'inserimento dell'indirizzo IP del target
path = input("Inserire il path scelto del sistema target: ") #variabile per l'inserimento del path target
port = 80 #variabile della porta predefinita


try: #ciclo try per intercettare errori nell'esecuzione
	connection = http.client.HTTPConnection(host, port) #gestisce la connessione verso l'host tramite il path inserito prendendo i parametri host e  port, restituendo l'oggetto connection>
	connection.request("OPTIONS", "/" +  path + ".html") #utilizzato per inviare una richiesta http specificando verbo e path
	response = connection.getresponse()
	metodi = response.getheader("allow").split(",") #inserimento della variabile dei metodi per divederli con lo split
	print("\nLa porta scansionata è la: ", port, "\nI metodi abilitati sono: ") #la risposta del server è prima salvata nella variabile response, poi verranno scritti a schermo i verbi hhtp abilitati in base alla risposta del server
	for i in range(len(metodi)): #ciclo for utilizzato per stampare in elenco i vari metodi abilitati, anziché stamparli in stringa
		print("[+] {}".format(metodi[i]))

	connection.close()

#Abbiamo inserito la request OPTIONS, lì avremmo potuto utilizzare uno degli altri verbi messi a disposizione.
#I parametri saranno diversi in base al verbo scelto.
#POST, ad es., può essere utilizzato per inviare informazioni al web server, come per una login.

except ConnectionRefusedError: #funzione che intercetta gli errori del ciclo try
	print("Connection Failed")