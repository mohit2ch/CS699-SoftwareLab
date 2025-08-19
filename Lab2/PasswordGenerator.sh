#!/bin/bash

function upper(){
	local s=ABCDEFGHIJKLMNOPQRSTUVWXYZ
	local index=$(($RANDOM % 26))
	echo -n ${s:$index:1}
}
function lower(){
	local s=abcdefghijklmnopqrstuvwxyz
	local index=$(($RANDOM % 26))
	echo -n ${s:$index:1}
}
function number(){
	local num=$(($RANDOM % 10))
	echo $num
}
function special(){
	local s="!@#$%^&*()_+"
	local index=$(($RANDOM % 12))
	echo -n ${s:$index:1}
}

echo "Enter the size of password to generate"
echo "(Generally Minimum 8, Recommended 16, Maximum 64)"
read PasswordLength

echo "Would you like to generate a 1.default openssl password or 2.customize this process?(1/2)"
read dOrc
PasswordGenerated=""
if [ $dOrc -eq 1 ]; then
	PasswordGenerated=$(openssl rand -base64 48 | cut -c1-$PasswordLength)
else
	echo "How many uppercase letters will there be?(1 - $PasswordLength)"
	read NumUpper
	PasswordLength=$(($PasswordLength-$NumUpper))
	echo "How many lowercase letters will there be?(1 - $PasswordLength)"
	read NumLower
	PasswordLength=$(($PasswordLength-$NumLower))
	echo "How many numbers will there be?(1 - $PasswordLength)"
	read NumNumbers
	PasswordLength=$(($PasswordLength-$NumNumbers))
	echo "Remaining $PasswordLength characters will be special characters"
	for i in $(seq 1 $NumUpper); do
		ch=$(upper)
		PasswordGenerated="$PasswordGenerated$ch"
	done
	for i in $(seq 1 $NumLower); do
		ch=$(lower)
		PasswordGenerated="$PasswordGenerated$ch"
	done
	for i in $(seq 1 $NumNumbers); do
		ch=$(number)
		PasswordGenerated="$PasswordGenerated$ch"
	done
	for i in $(seq 1 $PasswordLength); do
		ch=$(special)
		PasswordGenerated="$PasswordGenerated$ch"
	done
fi
echo $PasswordGenerated
