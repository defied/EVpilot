#!/bin/bash
# Requires sslsplit utility.
# Maybe one day you become python utility.

HIT=$(nslookup vkpilot.live-valkyrieapi.com | grep Address | grep -v '127.0' | cut -f 2 -d ' ')
HIT=$(echo $HIT | sed -r 's/ /,/g')
DIR=$1
EVE='eveLogger/'
SPLIT='sslsplit/'
HOST='10.0.51.254'

mkdir -p $DIR$SPLIT $DIR$EVE

#Route any traffic on port 443 to/from $HIT to port 8443.
iptables -t nat -A PREROUTING -p tcp -d $HIT --dport 443 -j REDIRECT --to-ports 8443
sleep 1
echo "##################"
echo "Re-directing traffic"
echo $(iptables -t nat -L | grep '8443')
echo "##################"

# Split traffic going through port 8443 out to files in $DIR.
sslsplit -D  -j $DIR$SPLIT -S ./ -k ca.key -c ca.crt https $HOST 8443 -S $DIR$EVE

# On teardown, remove redirect rule from iptables.
iptables -t nat -D PREROUTING -p tcp -d $HIT --dport 443 -j REDIRECT --to-ports 8443
sleep 1
iptables -t nat -D PREROUTING -p tcp -d $HIT --dport 443 -j REDIRECT --to-ports 8443
sleep 1
iptables -t nat -D PREROUTING -p tcp -d $HIT --dport 443 -j REDIRECT --to-ports 8443
sleep 1
iptables -t nat -D PREROUTING -p tcp -d $HIT --dport 443 -j REDIRECT --to-ports 8443
sleep 1
echo "##################"
echo "Resetting itpables"
echo $(iptables -t nat -L | grep '8443')
echo "##################"

# Bob's your uncle.
exit 0
