# BabyPi
Raspberry Pi with PiNoir Camera, IR LED, USB Microphone and DHT22 Adafruit Sensor

The stream will be available under the following address:
```
rtsp://YOURPILANADDRESS:80/live/picam
```

If you use VLC to connect to the stream, you can reduce the buffer size from 1000ms to e.g. 300ms to reduce the timelag.

## Overview

BabyPi needs no graphical interface, so it can be deactivated (boot into terminal with auto-login). SSH and camera module must be activated. However,configuring the ethernet or wifi settings is much more convenient with a GUI, so consider configuring them before turning to console-only mode.

```
sudo raspi-config
```

This setup uses picam and node-rtmp-rtsp-server from iizukanao. Picam is used to capture video and audio and the server is used to distribute it to LAN.

For temperature and humidity data the DHT22 sensor is beeing used. Data is logged and displayed through subtitle commands.

In addition to this, an IR LED-Cluster is installed and turned on in order to enable night vision (python scripts available).

The timezone can also be adjusted via commandline
```
sudo timedatectl set-timezone Europe/Berlin
```

=======
## BabyPi Scripts
First of all, from your home directory, clone this repo:
```
git clone https://github.com/GSAVV/BabyPi.git
```

## RTMP to RTSP Server

Node.js is integrated into Raspbian, but we need to install coffee script in order to make this work.

```
sudo apt-get install npm
sudo npm install --global coffeescript

git clone https://github.com/iizukanao/node-rtsp-rtmp-server.git
cd node-rtsp-rtmp-server
npm install -d
```
NPM thows some warning, saying its not compatible with current nodejs. But I just ignored it.

The server config can be edited with 'config.coffee'

Special thanks to https://hmbd.wordpress.com/2016/08/01/raspberry-pi-video-and-audio-recording-and-streaming-guide/


## picam

Picam is beeing used to capture and forward the video and audio. Also, it is used to integrate the subtitles

Installation
```
# dependencies
sudo apt-get update
sudo apt-get install libharfbuzz0b libfontconfig1

# picam
wget https://github.com/iizukanao/picam/releases/download/v1.4.9/picam-1.4.9-binary.tar.xz
tar xvf picam-1.4.9-binary.tar.xz
mkdir picam
cp picam-1.4.9-binary/picam ~/picam

# remove files
rm picam-1.4.9-binary.tar.xz
rm -r picam-1.4.9-binary/picam

# Create directories and symbolic links
cat > make_dirs.sh <<'EOF'
#!/bin/bash
DEST_DIR=~/picam
SHM_DIR=/run/shm

mkdir -p $SHM_DIR/rec
mkdir -p $SHM_DIR/hooks
mkdir -p $SHM_DIR/state
mkdir -p $DEST_DIR/archive

ln -sfn $DEST_DIR/archive $SHM_DIR/rec/archive
ln -sfn $SHM_DIR/rec $DEST_DIR/rec
ln -sfn $SHM_DIR/hooks $DEST_DIR/hooks
ln -sfn $SHM_DIR/state $DEST_DIR/state
EOF

./make_dirs.sh
```
Please notice, that the binary names may change in the future. iizukanao gives detailes instruction on how to compile new binaries from scratch.

## Startup Script

add the startup script to the /etc/rc.local file so it starts automatically with this line
```
/home/pi/BabyPi/BabyPi_start.sh &
```
The & is important!

## DHT22 Script

This script is started with the startup script. It reads the sensor data and creates the aubtitles and saves the data in a csv file.

You need Python2, which is usually pre-installed on Raspberry OS (you can type `python` and check the version number). 
Further, you need an (unfortunately) depreciated version of the adafruit_dht library. Install it with:
```
sudo pip install Adafruit_DHT
```

I will try to convert the code in the future to support Adafruits current tools.

However, we need to create the data log directory:
```
mkdir /home/pi/babylog
touch /home/pi/babylog/data.csv
```

If you want to access your data log via smb share, you have to make a samba 
share:
```   
sudo chmod 770 /home/pi/babylog 
sudo apt-get update 
sudo apt-get install samba samba-common smbclient 
sudo smbpasswd -a pi
sudo smbpasswd -a root
```

and add the following lines to the config file /etc/samba/smb.conf 
``` 
[Babylog]
   comment = Log directory of temperature and humidity data
   path = /home/pi/babylog
   browsable = yes
   read only = no
```

Reboot and your good to go!
