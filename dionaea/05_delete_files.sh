#!/bin/bash

MALWARE_DOWNLOAD_DIR='./downloads'

echo '[START]delete file and direcotry'
rm $MALWARE_DOWNLOAD_DIR/dionaea_malwares.tar
rm -rf $MALWARE_DOWNLOAD_DIR/home
rm -rf $MALWARE_DOWNLOAD_DIR/malware
echo '[FINISH]delete file and direcotry'
