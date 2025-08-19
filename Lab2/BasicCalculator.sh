#!/bin/bash

echo "This is a basic calculator that can compute basic mathematical expressions including additions and multiplications"
echo ""
option="Y"
while [ "$option" != "n" ];
do
    
    echo "Enter the expression to execute"
    read expression
    output=$((expression))
    echo "Output : $output"

    echo ""
    echo "Would you like to continue?(Y/n)"
    read option
done


