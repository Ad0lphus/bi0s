#include <stdio.h>
int main()
{
int a,b,c,d=0;
scanf("%d %d %d",&a,&b,&c);
while ((a+b)<=c || (b+c)<=a || (a+c)<=b)
{
d++;
if (b>=a && c>=a)
a++;
else if (a>=b && c>=b)
b++;
else
c++;
}
printf("%d",d);
return 0;
}

