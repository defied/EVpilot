#!/usr/bin/env python
import sys
import json
import curses
from curses import wrapper

#def main(stdscr):
#    # Clear screen
#    stdscr.clear()
#    # This raises ZeroDivisionError when i == 10.
#    for i in range(0, 11):
#        v = i-10
#        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
#    stdscr.refresh()
#    stdscr.getkey()

#wrapper(main)

#stdscr = curses.initscr()
teamid = []
fname = sys.argv[1]
jsonin = open(fname, 'r')
jsonfile = jsonin.read()
jsonfile = json.loads(jsonfile)
jsonin.close()
cleanup = { each['callsign'] : each for each in jsonfile['pilots'] }.values()
for i in cleanup:
   if 'team_id' in i:
      teamid.append(i)

teamid = sorted(teamid, key=lambda k: k['team_id'], reverse=False)
#teamid = json.dumps(teamid,indent=4,sort_keys=True)

for i in teamid:
   if i['team_id'] == 0:
      print(i['callsign'])
#print(teamid)
