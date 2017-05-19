#!/bin/bash

LogDir=/home/defied/eveLogger
DIR=/var/www/html/evevalkyrie/ValkyrieLIVE/


for i in $(cat $LogDir/*log | grep '"uri"' | grep -i amazon | cut -f 4 -d '"')
do
    tmpDir=$(echo $i | cut -f 4 -d '"' | cut -f 1 -d '?' | cut -f 6 -d '/')
    mkdir -p $DIR$tmpDir
done

for i in $(cat $LogDir/*log | grep '"uri"' | grep -i amazon | cut -f 4 -d '"')
do
    tmpDir=$(echo $i | cut -f 4 -d '"' | cut -f 1 -d '?' | cut -f 6,7 -d '/')
    curl $i > $DIR$tmpDir
done
