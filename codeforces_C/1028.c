#include <stdio.h>
int main()
{
int n,a,b,c,i;
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d %d %d",&a,&b,&c);
if(c%3==0)
printf("%d\n",a);
else if(c%3==1)
printf("%d\n",b);
else
printf("%d\n",a^b);
}
}
