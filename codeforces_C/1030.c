#include <stdio.h>
int main(){
int n,a,c=0;
scanf("%d",&n);
for(int i=0;i<n;i++){
scanf("%d",&a);
if(a==1)
c=c+1;
}
if(c>=1)
printf("HARD");
else
printf("EASY");
return 0;
}
