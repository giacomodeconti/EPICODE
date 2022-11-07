import math #Import per pi greco math.pi
def quadrato(): #Funzione perimetro quadrato
    per1= int(input('Inserisci il valore dal lato: '))
    print('Perimetro: ',per1*4)
def cerchio(): #Funzione circonferenza cerchio
    cer1= int(input('Inserisci il valore dal raggio: '))
    print('Circonferenza: ',cer1*math.pi*2)
def rettangolo(): #Funzione perimetro rettangolo
    ret1=int(input('Inserisci il valore della base '))
    ret2=int(input("Inserisci il valore dell'altezza "))
    print('Perimetro: ', ret1*2+ret2*2)
#Menu calcolatrice
while 1==1:
    ins1=input('CALCOLATORE\nPremi 1 perimetro del quadrato\nPremi 2 perimetro del rettangolo\nPremi 3 per circonferenza cerchio\nPremi 4 per uscire\n')
    if ins1=='1':
        quadrato()
    elif ins1=='2':
        rettangolo()
    elif ins1=='3':
        cerchio()
    elif ins1=='4':
        print('Exit')
        break #Interruzione programma
    else:
        print('')
        

