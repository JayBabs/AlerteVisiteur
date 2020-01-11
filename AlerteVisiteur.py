
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#######################################################
#Sujet : Reaction raspberryPI avec Système Camera Swann
#Auteur : Jeremie Babeu
#Date : 11 Novembre 2019
#######################################################
from datetime import datetime

import RPi.GPIO as GPIO
import time
import logging
from soco import SoCo
from soco.snapshot import Snapshot
from libsoundtouch import soundtouch_device
from libsoundtouch.utils import Source, Type



#################################
# 1. Methodes
#################################

# 1.1 Allumer la lumière

def allumerLED(): #the texting portion
    
    print ("LED on")
    GPIO.output(led,GPIO.HIGH)
   
# 1.2 Fermer la lumière     

def fermerLED():
    print("Lumiere off")
    GPIO.output(led,GPIO.LOW)

# 1.3 Jouer fichier wav sur Sonos 
def sonSonos():
       
    
       cuisine = SoCo('192.168.1.21')


       cuisine.volume =30 


       cuisine.play_uri('http://192.168.1.20/Sons/Sonnette.wav', title='alerte')
       
# 1.4 Jouer fichier wav sur Bose SoundTouch 1 
      

def sonBose1():
    nom = Entrepot 
    try:
        entrepot = soundtouch_device('192.168.1.11')
        entrepot.power_on()

        #entrepot.snapshot()
        volumeactuel = entrepot.volume()

        entrepot.set_volume(85)
        entrepot.play_url('http://192.168.1.39/Sons/Sonnette4.wav')
        time.sleep(4)

        #entrepot.restore()
        entrepot.set_volume(volumeactuel)

    except:
        logging.info('%s non disponible', nom)


# 1.5 Jouer le fichier wav sur Bose SoundTouch 2 

def sonBose2():
    nom = Laboratoire
    try:
        laboratoire = soundtouch_device('192.168.1.50')
        laboratoire.power_on()

        volumeactuel = laboratoire.volume()


        laboratoire.set_volume(85)
        laboratoire.play_url('http://192.168.1.39/Sons/Sonnette4.wav')
        time.sleep(4)

        laboratoire.set_volume(volumeactuel)

    except:
        logging.info('%s non disponible', nom)


def sonBose3():
    nom = bureau
    try:
        Bureau = soundtouch_device('192.168.1.116')
        Bureau.power_on()

        volumeactuel = Bureau.volume()

        Bureau.play_url('http://192.168.1.39/Sons/Sonnette4.wav')
        time.sleep(4)
        Bureau.set_volume(volumeactuel)
 
    except:
        logging.info('%s non disponible', nom)



def sonBose4():
    nom = Maison
    try:
        alerteMaison = soundtouch_device('192.168.1.113')
        alerteMaison.power_on()

        volumeactuel = alerteMaison.volume()


        alerteMaison.set_volume(80)
        alerteMaison.play_url('http://192.168.1.39/Sons/Sonnette4.wav')
        time.sleep(4)
        alerteMaison.set_volume(volumeactuel)

       
    except:
        logging.info('%s non disponible', nom)



#################################
# 2. Programme principale
#################################

# 2.1 Initialisation du RaspberryPI

led = 20
nvr = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(nvr,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led,GPIO.OUT)

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='Historique.log',level=logging.DEBUG)






# 2.2 Boucle principale 

while True:
    if GPIO.input(nvr)==0: # 2.2.1 Detection signal 
        
        # 2.2.2 Verification du jour de la semaine (0 = dimanche ) et l'heure sur format 00 à 24

        jourSemaine = datetime.today().strftime("%w")

        heureJournee = datetime.today().strftime("%H")

        jourSemaine = int(jourSemaine)
        
        heureJournee = int(heureJournee)

    
        


        
         

        
        if jourSemaine == 1 or jourSemaine == 2 or jourSemaine == 3 or jourSemaine == 4 or jourSemaine == 5:# 2.2.3 Horaire de semaine

            if heureJournee >= 7 and heureJournee <= 20:
                logging.info('Activitee legitime')
                
                sonBose1()
                sonBose2()
                sonBose3()
                sonBose4()
               
                
                time.sleep(60) #Sleep 1 minute
                
            else:
                 logging.info('Activite hors-horaire')
                 time.sleep(60) #Sleep 1 minute
                 

        if jourSemaine == 0 : # 2.2.4 Horaire dimanche
             if heureJournee >= 8 and heureJournee <= 18:
                logging.info("Activitee legitime")
        
                sonBose1()
                sonBose2()
                sonBose3()
                sonBose4()
               
                time.sleep(60) #Sleep 1 minute
                
             else:
                 logging.info("Activite hors-horaire")
                 time.sleep(60) #Sleep 1 minute
                 

        if jourSemaine == 6 : # horaire SAMEDI
            if heureJournee >= 8 and heureJournee <= 18:
                 logging.info("Activitee legitime")
                
                 sonBose1()
                 sonBose2()
                 sonBose3()
                 sonBose4()
                 
                 time.sleep(60) #Sleep 1 minute
            else:
                 logging.info("Activite hors-horaire")
                 time.sleep(60) #Sleep 1 minute
                




       
        
    else:
        
        time.sleep(5) #verification 5 secondes 
        
        logging.info('Rien a signaler')
 










