# importation
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib as mpl
from matplotlib import gridspec
import numpy as np

#--------------------------------------------------
# fonctions
def map(min1,max1,min2,max2,value2):
    a = (max1 - min1)/(max2 - min2)
    b = min1 - a * min2
    return a * value2 + b

#--------------------------------------------------
# extraction
theFile = open("Log.txt", "r")

GPS_tUnix = []
altitude = []
latitude = []
longitude = []
erreur_horizontale = []
erreur_verticale =[]
ALT_INTERVAL=100

WM_tUnix = []
temperature = []
humidite = []
pression = []

for line in theFile:
    values = line.split(',')
    if (values[0] == 'gps'):
        GPS_tUnix.append(float(values[1]))
        altitude.append(float(values[2]))
        latitude.append(float(values[3]))
        longitude.append(float(values[4]))
        erreur_horizontale.append(float(values[5]))
        erreur_verticale.append(float(values[6]))
    elif (values[0] == 'wm'):
        WM_tUnix.append(float(values[1]))
        temperature.append(float(values[4]))
        humidite.append(float(values[5]))
        pression.append(float(values[6]))

theFile.close()



# sortie test
print("---------------------")
print("\nGPS temps")
print(GPS_tUnix)
print("\nGPS altitude")
print(altitude)
print("\nGPS latitude")
print(latitude)
print("\nGPS longitude")
print(longitude)
print("\nGPS erreur H")
print(erreur_horizontale)
print("\nGPS erreur V")
print(erreur_verticale)
print("\n---------------------\n")
print("---------------------\n")
print("\nWM temps")
print(WM_tUnix)
print("\nWM température")
print(temperature)
print("\nWM humidité")
print(humidite)
print("\nWM pression")
print(pression)
print("\n---------------------\n")

print(len(pression))


#algorithme de sélection des paliers-----------------------------------------------------
paliers=[[],[]]

alt0=altitude[0]
t0=GPS_tUnix[0]

paliers[0].append(0)
paliers[1].append(int(alt0/ALT_INTERVAL)*ALT_INTERVAL)
k=1


for i in range(0,len(GPS_tUnix)):
    if int(altitude[i]/ALT_INTERVAL)*ALT_INTERVAL>=int(altitude[0]/ALT_INTERVAL)*ALT_INTERVAL+k*ALT_INTERVAL:
        k=k+1
        paliers[1].append(int(altitude[i]/ALT_INTERVAL)*ALT_INTERVAL)
        paliers[0].append(GPS_tUnix[i]-t0)
    if int(altitude[i]/ALT_INTERVAL)*ALT_INTERVAL<=int(altitude[0]/ALT_INTERVAL)*ALT_INTERVAL+(k-1)*ALT_INTERVAL and k!=1:
        k=k-1
        paliers[1].append(int(altitude[i]/ALT_INTERVAL)*ALT_INTERVAL)
        paliers[0].append(GPS_tUnix[i]-t0)

print(paliers[0])
print(paliers[1])

plt.plot(latitude,longitude)

plt.show()
