#! /usr/bin/python2.7
import serial
import urllib2
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)
pascode = "luce1a"
pascode1 = "luce2a"
while True:
  requ = urllib2.Request('http://localhost/php/lucesChecker.php')
  response1 = urllib2.urlopen(req).read()
  code1  = response1.find("luce1e")
  print response
  print code
  if pascode != code1:
    arduino.write("luce1e")
    print 'se prende'
  else
    arduino.write("luce1a")
    print 'se apaga'
  code = response1.find("luce2e")
  if pascode1 != code1:
    arduino.write("luce2e")
    print 'se prende'
  else
    arduino.write("luce2a")
    print 'se apaga'
  time.sleep(2)
