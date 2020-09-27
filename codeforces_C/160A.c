#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
int i,n,x=0,y=0,z=0,f=0,pass=1,temp;
scanf("%d",&n);
int *a;
a=(int *) malloc(n*sizeof(int));
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
x+=a[i];
}
while(f==0)
{
f=1;
for(i=0;i<n-pass;i++)
{
if(a[i]<a[i+1])
{
temp=a[i];
a[i]=a[i+1];
a[i+1]=temp;
f=0;
}
}
pass++;
}
for(i=0;i<n;i++)
{
y+=a[i];
z++;
if(y>x/2) break;
}
printf("%d\n",z);
return 0;
}

