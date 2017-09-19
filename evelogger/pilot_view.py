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
parser.add_argument('-d', '--directory', help='Directory containing json files to read.', required=True)

args = parser.parse_args()
pilot = args.pilot

pilot_file = 'pilots.json'
battle_file = 'active_battles_uri.json'
global_file = 'global_events.json'

def main():
    myscreen.refresh()
    teamid = get_team()
    init_count = 8
    team_0_colormap = 3
    team_1_colormap = 3
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
    myscreen.addstr(1, 1, "Pilot Squad Display v0.9.5", curses.A_BOLD)
    myscreen.addstr(1, 30, "{}".format(time.asctime()), curses.color_pair(3))
    #myscreen.addstr(2, 1, "Author: problah", curses.color_pair(3))
    #myscreen.addstr(2, 30, "Created: 9/13/2017", curses.color_pair(3))
    myscreen.addstr(init_count, 1, "Valkyrie", curses.color_pair(team_0_colormap) | curses.A_BOLD)
    init_count = init_count + 1
    for i in names_0:
        try:
            if init_count != len(names_0):
                team_mate = i
                platform = string.capitalize(string.split(names_0[i], ".")[1])
                myscreen.addstr(init_count, 5, team_mate, curses.color_pair(team_0_colormap))
                myscreen.addstr(init_count, 25, platform, curses.color_pair(team_0_colormap))
                if pilot in i:
                    myscreen.addstr(init_count, 1, "==>", curses.color_pair(team_0_colormap) | curses.A_BOLD)
                    myscreen.addstr(init_count, 5, team_mate, curses.color_pair(team_0_colormap) | curses.A_BOLD)
                    myscreen.addstr(init_count, 25, platform, curses.color_pair(team_0_colormap) | curses.A_BOLD)
        except:
            tmp = 'none'
        init_count = init_count + 1
    init_count = 8
    myscreen.addstr(init_count, 40, "Schism", curses.color_pair(team_1_colormap) | curses.A_BOLD)
    init_count = init_count + 1
    for i in names_1:
        try:
            if init_count != len(names_1):
                team_mate = i
                platform = string.capitalize(string.split(names_1[i], ".")[1])
                myscreen.addstr(init_count, 40, team_mate, curses.color_pair(team_1_colormap))
                myscreen.addstr(init_count, 60, platform, curses.color_pair(team_1_colormap))
                if pilot in i:
                    myscreen.addstr(init_count, 36, "==>", curses.color_pair(team_1_colormap) | curses.A_BOLD)
                    myscreen.addstr(init_count, 40, team_mate, curses.color_pair(team_1_colormap) | curses.A_BOLD)
                    myscreen.addstr(init_count, 60, platform, curses.color_pair(team_1_colormap) | curses.A_BOLD)
        except:
            tmp = 'none'
        init_count = init_count + 1
    # Time for the Battle Info.
    #
    battleinfo = get_battle()
    battlecount = 3
    server_port = "Server: {}:{}".format(battleinfo['public_ip'], battleinfo['port'])
    battleid = "Battle: {}".format(battleinfo['battle_id'])
    battlemap = string.split(battleinfo['map_unique_name'], '.')[1]
    battlemap = "Map: {}".format(battlemap)
    battlegame = string.split(battleinfo['game_mode_unique_name'], '.')[1]
    battlegame = "Game: {}".format(battlegame)
    try:
        myscreen.addstr(battlecount + 0, 1, server_port, curses.A_BOLD)
        myscreen.addstr(battlecount + 1, 1, battleid, curses.A_BOLD)
        myscreen.addstr(battlecount + 2, 1, battlemap, curses.A_BOLD)
        myscreen.addstr(battlecount + 3, 1, battlegame, curses.A_BOLD)
    except:
        myscreen.addstr()
        tmp = "None"
    # Now time for global info.
    #
    globalinfo = get_global()
    globalvisk = "Visk: {}".format(str(get_global()['visk']['visk']))
    globalbattles = "Battles: {}".format(globalinfo['battles']['battles_completed'])
    #globalvisk = "TestVisk"
    globalcount = 3
    try:
        myscreen.addstr(globalcount + 0, 40, globalvisk, curses.A_BOLD)
        myscreen.addstr(globalcount + 1, 40, globalbattles, curses.A_BOLD)
    except:
        myscreen.addstr()
        tmp = "None"


def get_team():
    teamid = []
    p_name = args.directory + pilot_file
    p_jsonin = open(p_name, 'r')
    p_jsonfile = p_jsonin.read()
    p_jsonfile = json.loads(p_jsonfile)
    p_jsonin.close()
    cleanup = { each['callsign'] : each for each in p_jsonfile['pilots'] }.values()
    for i in cleanup:
       if 'team_id' in i:
          teamid.append(i)
    teamid = sorted(teamid, key=lambda k: k['team_id'], reverse=False)
    return teamid

def get_battle():
    battleinfo = {}
    b_name = args.directory + battle_file
    b_jsonin = open(b_name, 'r')
    b_jsonfile = b_jsonin.read()
    b_jsonfile = json.loads(b_jsonfile)
    b_jsonin.close()
    for i in b_jsonfile:
        battleinfo[i] = b_jsonfile[i]
    return battleinfo

def get_global():
    globalinfo = {}
    #g_name = '/Users/Dafydd/Downloads/global_events.json'
    g_name = args.directory + global_file
    g_jsonin = open(g_name, 'r')
    g_jsonfile = g_jsonin.read()
    g_jsonfile = json.loads(g_jsonfile)
    g_jsonin.close()
    for i in g_jsonfile:
        globalinfo[i] = g_jsonfile[i]
    return globalinfo

def parse_team(id, teamid):
    team = []
    team_key = {}
    platform = []
    for i in teamid:
        if i['team_id'] == id:
            team_key[i['callsign']] = i['platform']
    return team_key

myscreen = curses.initscr()
curses.curs_set(False)
myscreen.border(0)
curses.start_color()

try:
    while True:
        main()
        time.sleep(1)
except:
    print "\nExiting\n"
    os.system('clear')
    os.system('reset')
