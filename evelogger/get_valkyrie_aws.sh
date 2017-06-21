#!/bin/bash

LogDir=/var/www/html/evevalkyrie/livepilot/files.json
DIR=/var/www/html/evevalkyrie/ValkyrieLIVE/


for i in $(cat $LogDir | grep '"uri"' | grep -i amazon | cut -f 4 -d '"')
do
    tmpDir=$(echo $i | cut -f 4 -d '"' | cut -f 1 -d '?' | cut -f 6 -d '/')
    mkdir -p $DIR$tmpDir
done

for i in $(cat $LogDir | grep '"uri"' | grep -i amazon | cut -f 4 -d '"')
do
    tmpDir=$(echo $i | cut -f 4 -d '"' | cut -f 1 -d '?' | cut -f 6,7 -d '/')
    curl $i > $DIR$tmpDir
done
