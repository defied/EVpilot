import os
import json
import glob
import sys
import time

logPath = '/home/defied/eveLogger/'
status = False
jsonFile = ""

def read_json_data(jfile):
    jdata = json.loads(jfile)
    return jdata

#def aws_json_collect():

def read_log(logPath, status, jsonFile):
    jres = {}
    count = 0
    diction = {}
    jsonFile = ""
    for files in glob.glob(logPath+"/*.log"):
        if "log" in files:
            for line in open(files):
                if "{" in line[0]:
                    status = True
                if status == True:
                    jsonFile = jsonFile + line
                if "}" in line[0]:
                    status = False
                    count = count + 1
                    diction[count] = jsonFile
                    jsonFile = ""
            for i in diction:
                jres[count] = read_json_data(diction[count])
            #os.remove(files)
            jsonFile = ""
        else:
            print "No log files found."
        return jres

def myprint(d):
    for k, v in d.iteritems():
        if isinstance(v, dict):
            print "{0}".format(k)#d.iterkeys().next())
            myprint(v)
        else:
            print "    {0} : {1}".format(k, v)

while True:
    if glob.glob(logPath+"/*.log"):
        jresa = read_log(logPath, status, jsonFile)
        for i in jresa:
            myprint(jresa[i])
            print ""
            print ""
    else:
        time.sleep(5)

