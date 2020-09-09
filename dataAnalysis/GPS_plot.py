import matplotlib.pyplot as plt

#----------------------------------------------------------------------
#------------EXTRACTION DU FICHIER FRIBOURG CHALLENGE-----------------------
#----------------------------------------------------------------------
theFile = open("Log.txt", "r")

GPS_tUnix = []
altitude = []
latitude = []
longitude = []
erreur_horizontale = []
erreur_verticale =[]

WM_tUnix = []
temperature = []
humidite = []
pression = []

GPS_INITIAL_TIME=0
WM_INITIAL_TIME=0

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

print(altitude)
print(latitude)
print(longitude)

print(max(longitude))
print(min(longitude))

print((max(latitude)))
print(min(latitude))

BBox = [6.8733,  7.7907, 46.3480, 46.8631]

ruh_m=plt.imread('fribourg2.png')


fig, ax = plt.subplots()
ax.set_title('Flight Itinerary')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
plt.plot(longitude,latitude, marker=None)
plt.show()