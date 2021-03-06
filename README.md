## EVpilot

A utility that will parse through the Unreal Engine API and present information to the user in a readable format.

--------------------
Note: Although this script was built using CCP's EVE: Valkyrie as reference, CCP considers is a violation of their EULA to use this utility on traffic generated from their client/server. Therefore:

#### "It is important to read the EULA of the product you are monitoring for any violations committed from the use of this software."

#### "This code is purely for educational purposes only and the author claims no responsibility, nor endorses, any activity or enhancement of this product for malicious intent, and cannot be held liable."
--------------------

#### You must install sslsplit

#### iptables must be running.

For updating, it's pretty simple:

### ./run_split.sh
1) Open a terminal window.

This will set up the iptable reroute and masking. You will need to run in the directory that has the cert keys (included).

2) edit run_split.sh and change $HOST to your gateway's Internal IP.

3) run ./run_split.sh /to/some/dir/

4) Open another terminal window.

### ./newParse.py

This will log and continually parse through output received from the UE4 services.

This should now also call for an update.

5) Create /to/some/dir/output/ directory.

6) from the git repo directory, run ./newParse.py -d /to/some/dir/eveLogger/ -o /to/some/dir/output/

7) Launch your UE4 application.

8) You should see run_split.sh terminal logging ssl connections.

9) Upon completion, ctrl-c in both terminals to end split and parsing.

10) Collect fullpilot.json from ~/output directory.

