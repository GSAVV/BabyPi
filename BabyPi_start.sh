#!/bin/bash
#rm -r /home/pi/picam/rec
#rm -r /home/pi/picam/hooks
#rm -r /home/pi/picam/state

mkdir -p /run/shm/rec
mkdir -p /run/shm/hooks
mkdir -p /run/shm/state
mkdir -p /home/pi/picam/archive

ln -sfn home/pi/picam/archive /run/shm/rec/archive
ln -sfn /run/shm/rec /home/pi/picam/rec
ln -sfn /run/shm/hooks /home/pi/picam/hooks
ln -sfn /run/shm/state /home/pi/picam/state

cd /home/pi/node-rtsp-rtmp-server/
./start_server.sh & # > /home/pi/rtmp-rtsp.log &
sleep 60
cd ..
cd picam/
./picam --alsadev hw:1,0 --rtspout  & # > /home/pi/picam.log &

