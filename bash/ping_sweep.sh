#!/bin/bash

if [ "$1" == "" ]
then
echo "[ERROR] No target given. Please, inform a target IP address"
echo "e.g.: $0 192.168.0"
else
for host in {1..254};do
# -w1 == 1 second; -c1 == 1 shot
# every address come with 64 bytes written
ping -w1 -c1 $1.$host | grep "64 bytes" | cut -d " ", -f4 | sed 's/.$/ is up./'
done
fi