#!/bin/bash

if [ $EUID -ne 0 ]; then
	echo ERROR: You must run this as root
	exit
fi

plymouthd --debug --debug-file=/tmp/plymouth-debug-out
# plymouthd
plymouth --show-splash
for ((I=0;I<10;I++)); do sleep 1 ; plymouth --update=event$I ; done ; 
plymouth --quit
plymouth quit
