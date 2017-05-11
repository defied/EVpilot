#!/usr/bin/python
# file_parsed['aipilots'][0]
# We want to re.split before the first { and after the last }.
# This is primarily to parse live web calls and get rid of the HTTP headers / Responses.
# print '{' + re.split('{', file2, maxsplit=1)[1]
# outTest = '{' + re.split('{', file2, maxsplit=1)[1]
# jsonSquad = json.loads(outTest)
# jsonSquad['pilots']
# jsonSquad['pilots'][0]
#
# TODO:
#   File should auto-parse web urls and attempt to download json files from aws server.
#       Need to find specific context to define these.
#           Try looking for '"branch_name": "ValkyrieLIVE"'
#           Next get httplib/urllib online to download these files to a custome dir structure.
#   Add Options parser to define:
#       Relate User
#       Obfuscate User
#       Directory to parse.
#       Intelligence to determine parse type and categorize.
#       Tab-delimited tree of information.
#       Information levels?
#       CSV output file (Tricky with subComponents)

import json
import re
import csv
import os
import glob
import sys
import time

fileName = 'AIPilots.json'

fileIn = open("{}".format(fileName), 'r')
fileRead = fileIn.read()
fileIn.close()
file_parsed = json.loads(fileRead)
fi_data = file_parsed['aipilots'] #"{}".format(keyFlags)]

# open a file for writing

file_data = open('/tmp/fileData.csv', 'w')

def cvs_write()
    # create the csv writer object
    csvwriter = csv.writer(file_data)
    count = 0
    for fi in fi_data:
          if count == 0:
                 header = fi.keys()
                 csvwriter.writerow(header)
                 count += 1
          csvwriter.writerow(fi.values())
    file_data.close()
