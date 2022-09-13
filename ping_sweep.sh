#!/bin/bash

for host in {1..254};do
# -w1 == 1 second; -c1 == 1 shot
# every address come with 64 bytes written
ping -w1 -c1 $1.$host | grep "64 bytes" | cut -d " ", -f4 | sed 's/.$/ is up./'
done
fi