#include<stdio.h>
#include<string.h>
int main()
{
int n;
char a[7],b[7],c[5],d[3],flag=0;;
scanf("%d",&n);
strcpy(a,"I hate");
strcpy(b,"I love");
strcpy(c,"that");
strcpy(d,"it");
printf("%s ",a);
if(n%2==0)
{
flag=1;
}
else
{
flag=0;
}
n--;
if(n!=0)
{
printf("%s ",c);
}
while(n!=0)
{
if(n%2==0&&flag==1)
{
printf("%s ",a);
}
else if(n%2==1&&flag==1)
{
printf("%s ",b);
}
else if(n%2==0&&flag==0)
{
printf("%s ",b);
}
else if(n%2==1&&flag==0)
{
printf("%s ",a);
}
if(n!=1)
{
printf("%s ",c);
}
n--;
}
printf("%s",d);
}

