# EVpilot

A utility that will parse through the E:V API and present information to the user in a readable format.
# You must install sslsplit

For Pilot updating, it's pretty simple:

./run_split.sh    
## This will set up the iptable reroute and masking. You will need to run in the directory that has the cert keys (included).
* edit run_split.sh and change $HOST to your gateway's Internal IP.

./newParse.py
## This will log and continually parse through live pilot output received from the EV services.
* Create ~/output directory.
./newParse.py ~/output


