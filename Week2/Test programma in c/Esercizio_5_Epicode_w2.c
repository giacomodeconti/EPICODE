#include <stdio.h>

void menu ();
void moltiplica ();
void dividi ();
void ins_string();
void bye (); // aggiunto funzione uscita
int check_one;
int check_two;

int main () 

{
	char scelta = '\0'; // erroe tolte le {} dallo 0
	menu ();
	label: // aggiunto label con il goto per reincominciare wuesta parte di codice in caso dovesse andare in default 
	scanf ("%c", &scelta); // primo errore %d ora in %c
	switch (scelta)
	{
		case 'A':
			moltiplica();
			break;
		case 'B':
            dividi();
            break;
		case 'C':
            ins_string();
            break;
        case 'D': // aggiunto case D per opzione di uscita + testo nel menu
        	bye();
        	break;
    default: // aggiunto default
    	printf("Scegli A, B, C o D\n");
    	rewind(stdin);
    	goto label;//aggiunto goto per tornare in cima
	}
return 0;}




void menu ()
{
	printf ("Benvenuto, sono un assitente digitale, posso aiutarti a sbrigare alcuni compiti\n");
	printf ("Come posso aiutarti?\n");
	printf ("A >> Moltiplicare due numeri\nB >> Dividere due numeri\nC >> Inserire una stringa\nD >> ESCI\n");

}


void moltiplica ()
{
	do{	//aggiunto il controllo delle lettere
	double  a,b,prodotto; //aggiunto double per accettare numeri grandi e le virgole
	printf ("Inserisci i due numeri da moltiplicare:");
	check_one = scanf ("%lf", &a); // errore é giusto %lf per aggiungere le virgole
	check_two = scanf ("%lf", &b); //aggiunto controllo uno e controllo due
	if(check_one==0||check_two==0){
		printf("Inserisci solo numeri\n");
		rewind(stdin);
	}
	else{
		prodotto = a * b;
		printf ("Il prodotto = %.2lf\n\n", prodotto); // aggiunta limitazione dopo la virgola
	}
	}while(check_one==0||check_two==0);//aggiunto il controllo delle lettere
}


void dividi ()
{
	do{	//aggiunto il controllo delle lettere
	double  a,b,divisione; //aggiunto double per accettare numeri grandi e le virgole
	rewind(stdin); 
    printf ("Inserisci il numeratore:");
    check_one = scanf ("%lf", &a);// errore é giusto %lf per aggiungere le virgole
    rewind(stdin); 
	printf ("Inserisci il denumeratore:");
    check_two = scanf ("%lf", &b);// errore é giusto %lf per aggiungere le virgole
	if(check_one==0||check_two==0){
		printf("\nInserisci solo numeri\n");
		rewind(stdin); 
	}
 	else{
    	divisione = a / b; // errore  c'é percentuale e non /
    	printf ("La divisione e': %.2lf", divisione); //aggiunto modifica testo
	}
    }while(check_one==0||check_two==0);
}

void ins_string () 
{
	char stringa[10]; //aggiunto limite 10 caratteri
        printf ("Inserisci la stringa massimo 10 caratteri:"); //aggiunto massimo 10 caratteri
        rewind(stdin);//aggiunto e pulito il buffer
        fgets(stringa, 10,stdin);//aggiunto fget per il controllo ed eliminiato lo scanf
        printf(stringa); // aggiunto il printf della stringa
}

void bye () //aggiunto funzione uscita
{
	printf("Ciao");
}
