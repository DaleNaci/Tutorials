#! /bin/bash

# ECHO COMMAND
echo Hello World!

# VARIABLE
# Uppercase by convention
# Letters, numbers, underscores
NAME="Brad"
echo "My name is ${NAME}"

# USER INPUT
read -p "Enter your name: " NAME
echo "Hello ${NAME}, nice to meet you!"

# SIMPLE IF STATEMENT
if [ "$NAME" == "Brad" ]
then
    echo "Your name is Brad"
fi

# IF-ELSE
if [ "$NAME" == "Brad" ]
then
    echo "Your name is Brad"
else
    echo "Your name is not Brad"
fi

# ELSE-IF (elif)
if [ "$NAME" == "Brad" ]
then
    echo "Your name is Brad"
elif [ "$NAME" == "Jack" ]
then
    echo "Your name is Jack"
else
    echo "Your name is not Brad or Jack"
fi
