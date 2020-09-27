#include<stdio.h>
#include<string.h>
int main(){
int i;
char a[100];
char b[100];
scanf("%s %s", a, b);

int val=strcasecmp(a, b);

if(val<0)
printf("-1\n");
if(val==0)
printf("0\n");
if(val>0)
printf("1\n");

return 0;
}
