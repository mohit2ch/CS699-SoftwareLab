#!/bin/bash
echo This is a tool to create a backup of files/folders and compress them
command="tar -c"

# tar -c Lab1-Website something.txt -f Example 
option="Y"
while [ "$option" != "n" ];
do
    echo Enter the absolute path of the file/folder
    read FileName
    command="$command $FileName"
    echo "Any more files to backup?(Y/n)"
    read option
    
    # option=$o
    
done
command="$command -f"
echo "What would you like to name the backup file"
read TarName
command="$command $TarName"
$($command)
# $($command)
