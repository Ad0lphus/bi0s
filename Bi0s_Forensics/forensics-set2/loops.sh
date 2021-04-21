#! /bin/bash
echo "hello worrld!"
echo "Loops Tasks"
echo "Pattern 1"
echo "========================"

for ((i=0;i<5;i++))
do
	for ((j=0;j<4-i;j++))
	do
		echo -n " "
	done
	for ((j=0;j<i+1;j++))
	do
		echo -n "#"
	done
		echo -e ""
	done
		echo ""

echo "Pattern 2: "
echo "======================"

for ((i=0;i<8;i++))
do
	for ((j=i;j<8;j++))
	do
		echo -n " "
	done
	for ((j=1; j<=i; j++))
	do
		echo -n "#"
	done
	for ((j=i-1;j>=1;j--))
	do
		echo -n "#"
	done
		echo
	done

