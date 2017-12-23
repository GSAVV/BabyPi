#!/bin/bash
mkdir -p /run/shm/rec/archive
mkdir -p /run/shm/hooks
mkdir -p /run/shm/state

ln -sfn /run/shm/rec/arvhive /home/pi/picam/archive

cd /home/pi/node-rtsp-rtmp-server/
./start_server.sh > /home/pi/rtmp-rtsp.log &
sleep 40
/home/pi/picam/picam --alsadev hw:1,0 --rtspout -w 800 -h 480 -v 500000 -f 20 > /home/pi/picam.log &

