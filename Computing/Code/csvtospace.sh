#!/bin/bash
# Author: Michael Jordan
# Script: csvtospace.sh
# Description:  Takes a csv file, converts to space delimited, and saves as a new file.
#
# Arguments: 1 -> csv delimited file. 2 -> new file name.
# Date: October 24, 2023

data="/mnt/c/Users/Michael Jordan/Desktop/MulQuaBio/data/Temperatures/$1"
if cat "$data" | grep -q "\,"
then
	echo "Creating a space delimited version of $1 and saving as $2.txt"
	cat "$data" | tr -s "," " " >> $2.txt
	echo "Done!"
else
	echo "Not a csv, sorry.  Can't help you."
fi
