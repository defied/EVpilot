#!/usr/bin/python
import json
import os

#fname='~/fullpilot.json'
#fname='/var/www/html/evevalkyrie/livepilot/fullpilotTEST.json'

def update(pfile, fname):
    header='{"pilots": '
    footer='}'
    pjson=json.loads(pfile)
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
        cleanup = sorted(cleanup, key=lambda k: k['pilot_id'], reverse=False)
        jsonfile['pilots']=cleanup
        with open(fname, 'w') as outfile:
            json.dump(jsonfile, outfile)
