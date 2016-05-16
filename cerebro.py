#! /usr/bin/python2.7
import serial
import urllib2
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)
while True:
  req = urllib2.Request('http://internetdelascosas.freeiz.com/test.php')
  response = urllib2.urlopen(req)
  code  = str(response.read())
  code = code[0:6]
  arduino.write(code)
  print (code)
  time.sleep(20)
