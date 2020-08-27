#!/bin/bash

if [ $EUID -ne 0 ]; then
	echo ERROR: You must run this as root
	exit
fi

plymouthd --debug --debug-file=/tmp/plymouth-debug-out
plymouth --show-splash
# sleep ${1:-2}
for ((I=0;I<3;I++)); do sleep 1 ; plymouth --update=event$I ; done ; 
plymouth quit
