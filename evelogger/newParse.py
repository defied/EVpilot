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
import argparse
import json
import re
import csv
import os
import glob
import sys
import time

# Set option flags.
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pilot', help='Bond data to specific pilot', required=False)
parser.add_argument('-l', '--list', help='list objects and components')
parser.add_argument('-o', '--object', help='Specify specific object to poll', default='')
parser.add_argument('-d', '--directory', help='Directory to read', required=True)
parser.add_argument('-v', '--hwVersion', help='Specify VMware Hardware Version. Default is 9.', default='9')

args = parser.parse_args()
#statLog.debug(args)

def myprint(d):
    ret = ''
    for k, v in d.iteritems():
        if isinstance(v, dict):
            ret = ret + "{0}".format(k)#d.iterkeys().next())
            myprint(v)
        else:
            ret = ret + "    {0} : {1}".format(k, v)

def json_list(directory):
    for fileName in glob.glob(logPath+"/*.log"):
        fileIn = open("{}".format(fileName), 'r')
        fileRead = fileIn.read()
        fileIn.close()
        file_parsed = json.loads(fileRead)
        objectOut = myprint(file_parsed)

def json_parser(objects, lists, file):
    fileIn = open("{}".format(fileName), 'r')
    fileRead = fileIn.read()
    fileIn.close()
    file_parsed = json.loads(fileRead)
    fi_data = file_parsed['aipilots'] #"{}".format(keyFlags)]


if args.list:
    json_list(args.directory)


def cvs_write():
    # open a file for writing
    file_data = open('/tmp/fileData.csv', 'w')
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
