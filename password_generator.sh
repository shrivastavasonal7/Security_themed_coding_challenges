#!/bin/bash

#Password Generator

echo " This is a Password Genrator"
echo " Please enter the length of the password: "
read PASS_LENGTH

for p in $(seq 1);
do
    openssl rand -base64 48 | cut -c1-$PASS_LENGTH      #Using openssl to create random characteers in base64 format using whole characteer range of base64 i.e. 48 and cutting it from column of first character to password length
done