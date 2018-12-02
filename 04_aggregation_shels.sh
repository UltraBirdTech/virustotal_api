#!/bin/bash

MALWARE_DOWNLOAD_DIR='./downloads'
HONEYPOT_DIR='home/honey/downloads'
DOWNLOAD_DIR='data/cowrie/downloads/*'

folder_num=$(ls $MALWARE_DOWNLOAD_DIR/$HONEYPOT_DIR | grep data* | wc -l)

echo '[START]aggregnation shell.'
echo "folder num is $folder_num"
if [ ! -e "$MALWARE_DOWNLOAD_DIR/malware" ]
  then
    mkdir $MALWARE_DOWNLOAD_DIR/malware
else
    rm $MALWARE_DOWNLOAD_DIR/malware/*
  fi

for i in `seq $folder_num`
do
  cp -pu $MALWARE_DOWNLOAD_DIR/$HONEYPOT_DIR/data$i/$DOWNLOAD_DIR $MALWARE_DOWNLOAD_DIR/malware
done

echo '[FINISH]aggregnation shell.'
