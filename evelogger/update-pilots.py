#!/usr/bin/python
import json
import string
import os
import sys

header='{"pilots": '
footer='}'

pilotFile=open('/var/www/html/evevalkyrie/livepilot/pilots.json', 'r')
pfile = pilotFile.read()
pilotFile.close()

pjson=json.loads(pfile)

fname='/var/www/html/evevalkyrie/livepilot/fullpilot.json'
os.path.isfile(fname)

if not os.path.isfile(fname):
    print "Creating {}".format(fname)
    jsonout=open(fname, 'w+')
    jsonout.write(pfile)
    jsonout.close()
else:
    print "{} exists. Consuming".format(fname)
    jsonin=open(fname, 'r')
    jsonfile=jsonin.read()
    jsonfile=json.loads(jsonfile)
    jsonin.close()
    jsonout=open(fname, 'w')
    jsonout.write(header)
    for i in pjson['pilots']:
        jsonfile['pilots'].insert(0, i)
    cleanup = { each['callsign'] : each for each in jsonfile['pilots'] }.values()
    jsonfile['pilots']=cleanup
    with open(fname, 'w') as outfile:
        json.dump(jsonfile, outfile)

