#include<stdio.h>
int main()
{
int i,n,c=1;
scanf("%d",&n);
char str[n];
char ch;
scanf("%c",&ch);
scanf("%s",str);
printf("%c",str[0]);
for(i=1;str[i]!='\0';)
{
c++;
printf("%c",str[i]);
i+=c;
}
printf("\n");
return 0;
}
