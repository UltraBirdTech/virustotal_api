#!/usr/bin/env python

import sys
import json
import urllib
import urllib2
import hashlib
import glob
from datetime import datetime
from time import sleep
import os

MALWARE_DIR = '/root/work/malware/downloads/malware/'

VIRUS_TOTAL_REPORT_URL = 'https://www.virustotal.com/vtapi/v2/file/report'

def main():
    print 'START SCRIPT'

    file_array = sorted(glob.glob( MALWARE_DIR + '*'), key=os.path.getmtime)
    i = 0 
    result_array = []

    for file in file_array:
       i += 1
       with open(file, 'rb') as f:
           hash = hashlib.sha256(f.read()).hexdigest()
           file_name = f.name.split("/")[-1]
           print '[LOG] Check: ' + file_name

       req = request_for_virustotal(hash)
       res = recieve_response(req)
       res_json = json.loads(res)

       permalink = ''
       file_detection_rate = ''
       if res_json['response_code'] == 0:
           print '===================[LOG] FAILED API======================'
           print res_json
       else:
         permalink = res_json["permalink"]
         file_detection_rate =  str(res_json["positives"]) + '/' + str(res_json["total"])

       time_float = os.path.getmtime(MALWARE_DIR + file_name)
       file_timedate = datetime.fromtimestamp(time_float).strftime("%Y/%m/%d %H:%M:%S")
       result_array.append("|" + file_name + "|" + file_timedate + "|" + file_detection_rate + "|" + permalink + "|")
       if 4 == i:
           print '[LOG] Sleep 65 seconds.'
           sleep(65)
           i = 0

    generate_output_file(result_array) 
    print 'END SCRIPT'
    exit()

def api_key():
    api_key_file_path = './api_key.txt'
    with open(api_key_file_path) as f:
      read = f.read()
      api_key = read.replace('\r', '')
      api_key = read.replace('\n', '')
    return api_key

def generate_data(data):
    parameters = {'resource': data, 'apikey': api_key()}
    return urllib.urlencode(parameters)

def request_for_virustotal(data):
    return urllib2.Request(VIRUS_TOTAL_REPORT_URL, generate_data(data))

def recieve_response(req):
    response = urllib2.urlopen(req)
    return response.read()

def generate_file_name():
    return 'virus_total_' + str(datetime.now().strftime("%Y%m%d%H%M%S")) + '.txt'

def header():
    return '|file name|date| kensyuturitu| URL |'

def constitution():
    return '|:--|:--|:--:|:--|'

def generate_output_file(array):
    f = open(generate_file_name(), 'w')
    f.writelines(header() + "\n")
    f.writelines(constitution() + "\n")
    for line in array:
        f.writelines(line + "\n")
    
    f.close()
main()
