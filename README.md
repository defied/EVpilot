# EVpilot

A utility that will parse through the E:V API and present information to the user in a readable format.
# You must install sslsplit

For Pilot updating, it's pretty simple:

1) Open a terminal window.
## ./run_split.sh    
# This will set up the iptable reroute and masking. You will need to run in the directory that has the cert keys (included).
2) edit run_split.sh and change $HOST to your gateway's Internal IP.
3) run ./run_split.sh
4) Open another terminal window.
## ./newParse.py
# This will log and continually parse through live pilot output received from the EV services.
# This should now also call for a pilot update.
5) Create ~/output directory.
6) from the git repo directory, run ./newParse.py -d ~/output
7) Launch EVE: Valkyrie
8) Play your brains out. You should see run_split.sh terminal logging ssl connections.
9) Upon completion, ctrl-c in both terminals to end split and parsing.
10) Collect fullpilot.json from ~/output directory.
11) Mail to defied@deadplanet.net



