#!/bin/bash

HONEYPOT_DIR='/root/work/honeypot'
MALWARE_DIR='/root/work/malware'
MALWARE_DOWNLOAD_DIR='/root/work/malware/downloads'
echo $HONEYPOT_DIR
echo $MALWARE_DIR

if [ ! -e $HONEYPOT_DIR/downloads.tar.gz ]
  then
    echo "Not Found File"
    exit 0
  else
    echo "Found File"
  fi

mv $HONEYPOT_DIR/downloads.tar.gz $MALWARE_DIR
gunzip -v $MALWARE_DIR/downloads.tar.gz
tar -xvf $MALWARE_DIR/downloads.tar -C $MALWARE_DIR

# sepalate from shell_01.sh. Maybe.. I should Shell_02.sh below scripts.
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
gunzip -v $MALWARE_DOWNLOAD_DIR/downloads.tgz.$i.gz
if [ ! -e $MALWARE_DOWNLOAD_DIR/data$i ]
  then
    echo 'create folder'
    mkdir $MALWARE_DOWNLOAD_DIR/data$i
  fi
tar -xzvf $MALWARE_DOWNLOAD_DIR/downloads.tgz.$i -C $MALWARE_DOWNLOAD_DIR/data$i
done