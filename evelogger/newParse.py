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
import io
import update_pilots

# Set option flags.
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pilot', help='Bond data to specific pilot', required=False)
parser.add_argument('-l', '--list', help='list objects and components', default='None')
parser.add_argument('-o', '--out', help='Where to write out JSON information', required=True)
parser.add_argument('-d', '--directory', help='Log directory to read', required=True)
parser.add_argument('-v', '--hwVersion', help='Specify VMware Hardware Version. Default is 9.', default='9')

args = parser.parse_args()
#statLog.debug(args)

# Declare variables.
# Start with the components you want to pull from the output.
headlist = ['callsign', 'training', 'pilots', 'files', 'global_events', 'squads', 'kills', 'squad_id','battle_uri',
            'active_battles_uri', 'heartbeat_count']
out_dir = args.out + 'fullpilot.json'
livedir = args.directory
ret = ''
output = []
#livedir = '/var/www/html/evevalkyrie/livepilot/'

# Check if outdir works.
if os.path.isdir(args.directory) == False:
    print "Directory {} does not exist.\neg: /var/www/html/evevalkyrie/livepilot/".format(livedir)
    sys.exit(165)

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
    for fi in file_data:
          if count == 0:
                 header = fi.keys()
                 csvwriter.writerow(header)
                 count += 1
          csvwriter.writerow(fi.values())
    file_data.close()

def list_collector():
    output = {}
    for fileName in glob.glob(args.directory+"/*.log"):
        try:
            output = json_list(fileName)
            #print output
        except:
            angry=False
            print "something broke"
    return output

def log_files(desc, data):
    print("Logging Files: {}".format(desc))
    with open("{}{}.json".format(args.out, header), 'w+') as f:
        if 'pilots' in header:
            print("Updating Pilot List")
            update_pilots.update(data, out_dir)
        f.write(data)
        f.close()

if args.out:
    print "Logging"

while True:
    print("Looking for logs...")
    time.sleep(5)
    printversion = ""
    for fileName in glob.glob(args.directory+"/*.log"):
        print('Ingesting {}'.format(fileName))
        try:
            print("importing list: {}".format(fileName))
            output = json_list(fileName)
            for header in headlist:
                if header in output:
                    print("Collecting {}".format(header))
                    printversion = ""
                    log_files(header, json.dumps(output, indent=4, sort_keys=True))
        except:
            angry=False
            print "I hate you."
        try:
            os.remove(fileName)
        except:
            angry=False
            print "Error. Failed to remove file {}".format(fileName)

