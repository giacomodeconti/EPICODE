#include<stdio.h>
#include<stdlib.h>
int main (){
	while(1==1){
		int contr;
		char name[20];// name lenght check max 20
		int point=0; // point
		int val; // input value
		printf ("Quiz game\nFor start press 1  otherwise  digit any key to exit\n"); // game start or shut down
		scanf ("%d",&val);
		if (val==1){
			printf("Type your name ");
  			rewind(stdin); // clear buffer
  			fgets(name, 20,stdin); // name lenght check max 20
  			printf("\nYour name is : %s\n\nPRESS ENTER to start", name); // name print
  			getch(); // starts game
  			system("cls"); //clear command line
  			do{ // initial loop fro answer check
			printf ("Which is the first letter in afabet?\n\nChoose:\n\n1) b\n2) c\n3) a\n"); // first question
			rewind(stdin); // clear buffer
			contr=scanf ("%d",&val); // input
			if (val==3){
				point++;} // point +1
			else {}
			}while(val<1||val>3||contr==0); // rule for do and answre check			
			system("cls");
			do{ // initial loop fro answer check
			rewind(stdin); // clear buffer
			printf ("Which is the second letter in afabet?\n\nChoose:\n\n1) b\n2) c\n3) a\n"); // second question
			contr=scanf  ("%d",&val); // input
			if (val==1){
				point++;} // point +1
			else {}
			}while(val<1||val>3||contr==0); // rule for do and answre check
			system("cls");
			do{ // initial loop fro answer check
			rewind(stdin); // clear buffer
			printf ("1+2=?\n\nChoose:\n\n1) 1\n2) 2\n3) 3\n"); // third question
			contr=scanf  ("%d",&val); // input
			if (val==3){
				point++;} // point +1
			else{}
			}while(val<1||val>3||contr==0); // rule for do and answre check
			printf("\n\nHI! %s", name); // print name
			printf ("\nYOU GOT %d POINTS\n\n",point); // print results
			printf ("\nPRESS ANY KEY TO CONTINUE\n\n");
			getch(); // game restart	
			system("cls");}
		else if (val!=1){
			system("cls");
			printf ("installing WannaCry...\n\nSend me some bitcoin");
			break;}} // stop program
return 0;}
