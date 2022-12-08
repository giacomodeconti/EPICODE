#include<stdio.h>
int main (){
    char buffer[10];
    printf("Type username\n");
    //scanf("%s", buffer);	wrong command 
    fgets(buffer,10,stdin); // right one, for cut the legnght of a string
    printf("\nYour username is : %s\n", buffer); 
return 0;}
