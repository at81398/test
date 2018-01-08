import sys
import time
import httplib, urllib
import json
import Adafruit_DHT
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while 1:
	SwitchStatus = GPIO.input(5)
	if( SwitchStatus == 0):
                print('***ON***')
        else:
                print('***OFF***')
	time.sleep(1)
