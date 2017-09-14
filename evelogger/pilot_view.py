#!/usr/bin/env python
import sys
import json
import curses
import time
import os
import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pilot', help='Pilot name.', required=True)
parser.add_argument('-d', '--directory', help='pilot json file to read.', required=True)

args = parser.parse_args()
pilot = args.pilot

def main():
    myscreen.refresh()
    teamid = get_team()
    init_count = 7
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    names_0 = parse_team(0, teamid)
    for i in names_0:
        if pilot in i:
            team_0_colormap = 2
            team_1_colormap = 1
    names_1 = parse_team(1, teamid)
    for i in names_1:
        if pilot in i:
            team_0_colormap = 1
            team_1_colormap = 2
    myscreen.addstr(1, 1, "Pilot Squad Display v0.9", curses.A_BOLD)
    myscreen.addstr(1, 30, "{}".format(time.asctime()), curses.color_pair(3))
    myscreen.addstr(2, 1, "Authors: SuperKev, problah", curses.color_pair(3))
    myscreen.addstr(2, 30, "Created: 9/13/2017", curses.color_pair(3))
    myscreen.addstr(5, 10, "Valkyrie", curses.color_pair(team_0_colormap) | curses.A_BOLD)
    for i in names_0:
        try:
            if init_count != len(names_0):
                team_mate = i
                platform = string.capitalize(string.split(names_0[i], ".")[1])
                myscreen.addstr(init_count, 10, team_mate, curses.color_pair(team_0_colormap))
                myscreen.addstr(init_count, 30, platform, curses.color_pair(team_0_colormap))
                if pilot in i:
                    myscreen.addstr(init_count, 6, "==>", curses.color_pair(team_0_colormap) | curses.A_BOLD)
                    myscreen.addstr(init_count, 10, team_mate, curses.color_pair(team_0_colormap) | curses.A_BOLD)
                    myscreen.addstr(init_count, 30, platform, curses.color_pair(team_0_colormap) | curses.A_BOLD)
        except:
            tmp = 'none'
        init_count = init_count + 1
    myscreen.addstr(5, 50, "Schism", curses.color_pair(team_1_colormap) | curses.A_BOLD)
    init_count = 7
    for i in names_1:
        try:
            if init_count != len(names_1):
                team_mate = i
                platform = string.capitalize(string.split(names_1[i], ".")[1])
                myscreen.addstr(init_count, 50, team_mate, curses.color_pair(team_1_colormap))
                myscreen.addstr(init_count, 70, platform, curses.color_pair(team_1_colormap))
                if pilot in i:
                    myscreen.addstr(init_count, 46, "==>", curses.color_pair(team_1_colormap) | curses.A_BOLD)
                    myscreen.addstr(init_count, 50, team_mate, curses.color_pair(team_1_colormap) | curses.A_BOLD)
                    myscreen.addstr(init_count, 70, platform, curses.color_pair(team_1_colormap) | curses.A_BOLD)
        except:
            tmp = 'none'
        init_count = init_count + 1

def get_team():
    teamid = []
    fname = args.directory
    #fname = "/Users/Dafydd/Downloads/pilots.json"
    jsonin = open(fname, 'r')
    jsonfile = jsonin.read()
    jsonfile = json.loads(jsonfile)
    jsonin.close()
    cleanup = { each['callsign'] : each for each in jsonfile['pilots'] }.values()
    for i in cleanup:
       if 'team_id' in i:
          teamid.append(i)
    teamid = sorted(teamid, key=lambda k: k['team_id'], reverse=False)
    return teamid

def parse_team(id, teamid):
    team = []
    team_key = {}
    platform = []
    for i in teamid:
        if i['team_id'] == id:
            team_key[i['callsign']] = i['platform']
            # team.append(i['callsign'])
            # platform.append(i['platform'])
    return team_key


##teamid = json.dumps(teamid,indent=4,sort_keys=True)




myscreen = curses.initscr()
curses.curs_set(False)
myscreen.border(0)
curses.start_color()

try:
    while True:
        main()
except:
    print "\nExiting\n"
    os.system('clear')
    os.system('reset')



# for i in names:
#     if pilot in i:
#         print("found {}".format(pilot))

# teamid = get_team()
# names, count = parse_team(0, teamid)
# for i in names:
#     print(i)
# print(count)
# #print teamid
# print(len(parse_team()))
