#include <stdio.h>
#include <math.h>
#include <string.h>

int main(void) {
char s[101];
scanf("%s", s);
if (strlen(s) == 1) {
printf("%s", s);
}
else {
int ones = 0;
int twos = 0;
int threes = 0;
for (int i = 0; i < strlen(s); i++) {
if (s[i] == '1') {
ones++;
}
else if (s[i] == '2') {
twos++;
}
else if (s[i] == '3') {
threes++;
}
}
char out[strlen(s)+1];
int k = 0;
for (int j = 0; j < strlen(s); j++) {
if (j % 2 == 0) {
if (k < ones) {
out[j] = '1';
k++;
}
else if (k < ones + twos) {
out[j] = '2';
k++;
}
else if (k < ones + twos + threes) {
out[j] = '3';
k++;
}
}
else {
out[j] = '+';
}
}
out[strlen(s)] = '\0';
printf("%s", out);
}
}
