# BabyPi
Raspberry Pi with PiNoir Camera, IR LED, USB Microphone and DHT22 Adafruit Sensor

## Overview

BabyPi needs no graphical interface, so it can be deactivated (boot into terminal with auto-login). SSH and camera module must be activated

```
sudo raspi-config
```

This setup uses picam and node-rtmp-rtsp-server from iizukanao. Picam is used to capture video and audio and the server is used to distribute it to LAN.

For temperature and humidity data the DHT22 sensor is beeing used. Data is logged and displayed through subtitle commands.

In addition to this, one or mutliple IR LEDs are installed and turned on in order to enable night vision.


## RTMP to RTSP Server

Node.js is integrated into Raspbian, but we need to install coffee script in order to make this work.

```
sudo apt-get install npm
sudo npm install coffee-script -g

git clone https://github.com/iizukanao/node-rtsp-rtmp-server.git
cd node-rtsp-rtmp-server
npm install -d
```

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
wget https://github.com/iizukanao/picam/releases/download/v1.4.6/picam-1.4.6-binary-stretch.tar.xz
tar xvf picam-1.4.6-binary-scetch.tar.xz
cp picam-1.4.6-binary-stretch/picam ~/picam/
cp picam-1.4.6-binary-stretch/LICENSE ~/picam/

# remove files
rm picam-1.4.6-binary-scetch.tar.xz
rm -r picam-1.4.6-binary-scetch/picam
```
Please notice, that the binary names may change in the future. iizukanao gives detailes instruction on how to compile new binaries from scratch.

## Startup Script

... to be done

## DHT22 Script

... to be done



