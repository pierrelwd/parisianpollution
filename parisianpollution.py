#!/usr/bin/python
# -*- coding: latin-1 -*-

import urllib, json
import time
from os import chdir

#Get data from AirParif API
url = "http://www.airparif.asso.fr/appli/api/indice?date=jour"
apiResponse = urllib.urlopen(url);

#Get the Json
rawData = json.loads(apiResponse.read());

#Data by pollution type
globalData = (rawData["global"])
no2Data = (rawData["no2"])
o3Data = (rawData["o3"])
pm10Data = (rawData["pm10"])

#Open a directory to save sata
chdir("/tmp")

#Give a name to the file
#If the file do not exist, it will create it
#If it already exists, it will open it
fileName = str(time.strftime('%y-%m'))+"-pollutionrecord"

#Select the file
file = open(fileName, "a")

#Save data
file.write(str(time.strftime('%y-%m-%d'))+";"+
str((globalData["indice"]))+";"+str((no2Data["indice"]))+";"+
(str((o3Data["indice"]))+";"+(str((pm10Data["indice"]))+"\n")))

#Close the file
file.close()
