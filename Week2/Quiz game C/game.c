#include<stdio.h>
int main (){
	int val; // input value
	int point; // point
	int cl=1; // while cicle
	while(cl==1){
		printf ("Quiz game\nFor start press 1  otherwise  press 2\n"); // game start or shut down
		scanf ("%d",&val);
		if (val==1){
			printf ("\n\nWhich is the first letter in afabet?\n\nChoose:\n\n1) b\n2) c\n3) a\n");
			scanf ("%d",&val);
			if (val==3){
				point++;
				printf ("\n\nmmm yess you got one point baby\n\n\n");}	
			else {
				printf("nice idiot\n\n");}
			printf ("\n\nWhich is the second letter in afabet?\n\nChoose:\n\n1) b\n2) c\n3) a\n");
			scanf  ("%d",&val);
			if (val==1){
				point++;
				printf ("you are like a genius, one more point for you\n\n\n");}
			else {
				printf("go home\n\n");}
			printf ("1+2=?\n\nChoose:\n\n1) 1\n2) 2\n3) 3\n");
			scanf  ("%d",&val);
			if (val==3){
				point++;
				printf ("\nnice work Einstein\n\n");}
			else{
				printf ("\ngo to school\n\n");}
			printf ("\nYOU GOT %d POINTS\n\n",point);
			point=0;
			printf ("\nTHE GAME WILL RESTART\n\n");}		
		else if (val==2){
			printf ("ok pussy");
			cl=0;}}
return 0;}

	
		
	


	
