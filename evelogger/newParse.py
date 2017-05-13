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
#   Add arg parser to:
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
import string

# Declare variables.
ret = ''
output = []

# Set option flags.
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pilot', help='Bond data to specific pilot', required=False)
parser.add_argument('-l', '--list', help='list objects and components', default='None')
parser.add_argument('-o', '--out', help='Where to write out JSON information', action='store_true', default=False)
parser.add_argument('-d', '--directory', help='Log directory to read', required=True)
parser.add_argument('-v', '--hwVersion', help='Specify VMware Hardware Version. Default is 9.', default='9')

args = parser.parse_args()
#statLog.debug(args)


def json_list(fileName):
    try:
        fileIn = open("{}".format(fileName), 'r')
        fileRead = fileIn.read()
        try:
            fileRead = '{' + re.split('{', fileRead, maxsplit=1)[1]
        except:
            notSoMuch=False
        fileIn.close()
        try:
            file_parsed = json.loads(fileRead)
            return file_parsed
        except:
            parse=False
    except:
        Fail=True

def myprint(d):
    ret = ''
    for k, v in d.iteritems():
        if isinstance(v, dict):
            ret = ret + "{0}".format(d.iterkeys().next())
            #myprint(v)
        else:
            ret = ret + "{0}".format(d.iterkeys().next())
        return ret

def json_parser(objects, lists, file):
    fileIn = open("{}".format(file), 'r')
    fileRead = fileIn.read()
    fileIn.close()
    file_parsed = json.loads(fileRead)

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

def list_collector():
    output = []
    for fileName in glob.glob(args.directory+"/*.log"):
        try:
            output = json_list(fileName)
            #print output
        except:
            angry=False
            print "something broke"
    return output

# Gather the latest output:
output = list_collector()

# print "Checking list argument:\n    {}".format(args.list)
for fileName in glob.glob(args.directory+"/*.log"):
    try:
        outputlist = json_list(fileName).keys()
        output = json_list(fileName)
        for i in output:
            # List server
            # if args.list in i:
            #     print " "
            #     print "####"
            #     print output
            if 'branch_name' in i:
                print ""
                print "####"
                for files in output['files']:
                    if args.out:
                        placer=False
                    print files['uri']

                #print "Created on: {}".format(output['create_date'])
            # print output['pilots'][0]['platform']
            # print output['pilots'][0]['team_id']
        # if 'all' not in args.list and args.object in output:
        #     print "got a hit."
        #     print output
    except:
        angry=False
        #print "nope"
if args.out:
    print "Logging"

