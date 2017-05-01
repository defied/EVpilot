#!/bin/bash
iptables -t nat -A PREROUTING -p tcp -d 52.48.94.106,52.51.224.61,52.18.156.124 --dport 443 -j REDIRECT --to-ports 8443
sleep 1
echo "##################"
echo $(iptables -t nat -L | grep '8443')
echo "##################"
echo "Hit Enter to Continue"
read
#sslsplit -D -j /tmp/sslsplit/ -S ./ -k ca.key -c ca.crt ssl 10.0.51.254 8443 -L /root/evelogger/pipe
sslsplit -D  -j /tmp/sslsplit/ -S ./ -k ca.key -c ca.crt https 10.0.51.254 8443 -S /root/evelogger/logs/
iptables -t nat -D PREROUTING -p tcp -d 52.48.94.106,52.51.224.61,52.18.156.124 --dport 443 -j REDIRECT --to-ports 8443
sleep 1
echo "##################"
echo $(iptables -t nat -L | grep '8443')
echo "##################"
exit 0
