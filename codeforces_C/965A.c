#include<stdio.h>

int main()
{
int k,n,s,p,a=0;
scanf("%d %d %d %d",&k,&n,&s,&p);
if(n%s==0)
n=n/s;
else
n=n/s+1;
k=k*n;
for(s=1;;s++)
{
a=a+p;
if(a>=k)
break;
}
printf("%d\n",s);
}
