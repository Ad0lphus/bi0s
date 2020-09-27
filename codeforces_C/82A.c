#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
int main(){
int count ,trail,num;
scanf("%d",&num);
for(count=0,trail=0;trail<num;trail+=5*pow(2,count),count++)
;
count--;
trail-=5*pow(2,count);
count=pow(2,count);
num--;
if((num-trail)/count==0)
printf( "Sheldon");
else if ((num-trail)/count==1)
printf( "Leonard");
else if ((num-trail)/count==2)
printf( "Penny");
else if ((num-trail)/count==3)
printf( "Rajesh");
else if((num-trail)/count==4)
printf(  "Howard");
return 0;
}
