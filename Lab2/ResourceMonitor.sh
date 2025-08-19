#!/bin/bash

echo "This is Resource Monitor that shows the top 5 processes that use most cpu and memory."
echo "Press Ctrl+C to exit"

while true; do
clear

echo "__________________________________________________________________________________"
echo ""
echo "Top 5 by Memory consumption\n"
echo "$(ps -e -o pid,ppid,comm,pmem --sort=-%mem | head -n 6)"
echo ""
echo "__________________________________________________________________________________"
echo ""
echo "Top 5 by CPU consumption\n"
echo "$(ps -e -o pid,ppid,comm,pcpu --sort=-%cpu | head -n 6)"
echo ""
echo "__________________________________________________________________________________"

sleep 5
done

