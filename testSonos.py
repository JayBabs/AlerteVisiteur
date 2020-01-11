#!/usr/bin/env python
# -*- coding: utf-8 -*-

#######################################################
#Sujet : Test Sonos
#Auteur : Jérémie Babeu
#Date : 11 Novembre 2019
#######################################################

import RPi.GPIO as GPIO
import time
from soco import SoCo
from soco.snapshot import Snapshot




def sonBose1():
    
    entrepot = soundtouch_device('192.168.1.11')
    entrepot.power_on()

    #entrepot.snapshot()
    volumeactuel = entrepot.volume()



    entrepot.set_volume(25)
    entrepot.play_url('http://192.168.1.39/Sons/Sonnette.wav')
    time.sleep(2)
    entrepot.play_url('http://192.168.1.39/Sons/Sonnette.wav')
    time.sleep(2)





    #entrepot.restore()
    entrepot.set_volume(volumeactuel)

sonBose1()
