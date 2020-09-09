
import numpy as np
#----------------------------------------------------------------------
#------------EXTRACTION DU FICHIER COSMIC HUNTER-----------------------
#----------------------------------------------------------------------
theFile = open("data_cosmic_hunter.txt", "r")

num = []
second = []
record_time = []
TOP = []
BOTTOM = []
ext = []
coincidence = []
intern_pressure=[]
intern_temperature=[]
intern_humidity=[]
i = 0

#----------------------------Lecture des données----------------
for value in theFile.read().split():
    if (i >= 4 or i==0) :
        if (i == 0): num.append(value)
        elif (i == 4) : second.append(value)
        elif (i == 5) : record_time.append(value)
        elif (i == 6) : TOP.append(value)
        elif (i == 7) : BOTTOM.append(value)
        elif (i == 8) : ext.append(value)
        elif (i == 9) : coincidence.append(value)
        elif (i == 10): intern_pressure.append(value)
        elif (i == 11): intern_temperature.append(value)
        elif (i == 12):
            intern_humidity.append(value)
            i=-1
    i += 1
theFile.close()


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

#traitement pour avoir un temps commun avec le cosmic hunter

GPS_INITIAL_TIME = GPS_tUnix[0]
GPS_time=[]
for i in range(0,len(GPS_tUnix)):
    GPS_time.append(int(GPS_tUnix[i])-int(GPS_INITIAL_TIME))

WM_INITIAL_TIME = WM_tUnix[0]
WM_time=[]
for i in range(0,len(WM_tUnix)):
    WM_time.append(int(WM_tUnix[i])-int(WM_INITIAL_TIME))

print("temps unifiés")
print(WM_time)
print(GPS_time)

#----------------------------------------------------------------------
#------------TRAITEMENT DES DONNEES------------------------------------
#----------------------------------------------------------------------

#-----------------------traitement des données pour avoir un fichier unique--------------------------


#Altitude
mean_altitude=[]
mean_altitude.append(0)
mean_altitude.append(0)
mean_altitude_error=[]
mean_altitude_error.append(0)
mean_altitude_error.append(0)
current_data_alt=[]
#Longitude
mean_long=[]
mean_long.append(0)
mean_long.append(0)
mean_long_error=[]
mean_long_error.append(0)
mean_long_error.append(0)
current_data_long=[]
#Latitude
mean_lat=[]
mean_lat.append(0)
mean_lat.append(0)
mean_lat_error=[]
mean_lat_error.append(0)
mean_lat_error.append(0)
current_data_lat=[]

#Temperature
mean_temp=[]
mean_temp.append(0)
mean_temp.append(0)
mean_temp_error=[]
mean_temp_error.append(0)
mean_temp_error.append(0)
current_data_temp=[]

#Pressure
mean_p=[]
mean_p.append(0)
mean_p.append(0)
mean_p_error=[]
mean_p_error.append(0)
mean_p_error.append(0)
current_data_p=[]

#Humidity
mean_h=[]
mean_h.append(0)
mean_h.append(0)
mean_h_error=[]
mean_h_error.append(0)
mean_h_error.append(0)
current_data_h=[]



for i in range(2,len(num)):
    final_time=int(second[i])
    initial_time=int(final_time)-600
    for j in range (0,len(GPS_time)):
        if (GPS_time[j]>=initial_time and GPS_time[j]<=final_time):
            current_data_alt.append(float(altitude[j]))
            current_data_long.append(float(longitude[j]))
            current_data_lat.append(float(latitude[j]))
            current_data_temp.append(float(temperature[j]))
            current_data_p.append(float(pression[j]))
            current_data_h.append(float(humidite[j]))

    mean_altitude.append(np.mean(current_data_alt))
    mean_altitude_error.append(np.std(current_data_alt))
    current_data_alt=[]

    mean_long.append(np.mean(current_data_long))
    mean_long_error.append(np.std(current_data_long))
    current_data_long=[]

    mean_lat.append(np.mean(current_data_lat))
    mean_lat_error.append(np.std(current_data_lat))
    current_data_lat = []

    mean_temp.append(np.mean(current_data_temp))
    mean_temp_error.append(np.std(current_data_temp))
    current_data_temp = []

    mean_p.append(np.mean(current_data_p))
    mean_p_error.append(np.std(current_data_p))
    current_data_p = []

    mean_h.append(np.mean(current_data_h))
    mean_h_error.append(np.std(current_data_h))
    current_data_h = []

print("Altitude")
print(mean_altitude)
print(mean_altitude_error)

print("Longitude")
print(mean_long)
print(mean_long_error)

print("Latitude")
print(mean_lat)
print(mean_lat_error)

print("Temperature")
print(mean_temp)
print(mean_temp_error)

print("Pressure")
print(mean_p)
print(mean_p_error)

print("Humidité")
print(mean_h)
print(mean_h_error)

print(len(num))
print(len(mean_altitude))



#----------------------------------------------------------------------
#------------creation d'un nouveau fichier------------------------------------
#----------------------------------------------------------------------

file = open("flight_data.txt", "w")

file.write("num"+"\t"+"sec"+"\t"+"rec_time"+"\t"+"TOP"+"\t"+"BOTTOM"+"\t"+"EXT"+"\t"+"COINC"+"\t"+"Int_pressure"+"\t"+"Int_Temp"+"\t"+"Int_Hum"+"\t"+"mean_alt"+"\t"+"mean_alt_error"+"\t"+"Mean_latitude"+"\t"+"Mean_latitude_error"+"\t"+"Mean_longitude"+"\t"+"Mean_longitude_error"+"\t"+"Mean_temperature"+"\t"+"Mean_temperature_error"+"\t"+"Mean_pressure"+"\t"+"Mean_pressure_error"+"\t"+"Mean_humidity_error"+"\t"+"Mean_humidity_error"+"\n")

for i in range(2,len(num)):
    file.write(str(num[i])+"\t"+str(second[i])+"\t"+str(record_time[i])+"\t"+str(TOP[i])+"\t"+str(BOTTOM[i])+"\t"+str(ext[i])+"\t"+str(coincidence[i])+"\t"+str(intern_pressure[i])+"\t"+str(intern_temperature[i])+"\t"+str(intern_humidity[i])+"\t"+str(mean_altitude[i])+"\t"+str(mean_altitude_error[i])+"\t"+str(mean_lat[i])+"\t"+str(mean_lat_error[i])+"\t"+str(mean_long[i])+"\t"+str(mean_long_error[i])+"\t"+str(mean_temp[i])+"\t"+str(mean_temp_error[i])+"\t"+str(mean_p[i])+"\t"+str(mean_p_error[i])+"\t"+str(mean_h[i])+"\t"+str(mean_h_error[i])+"\n")
file.close()

print(num)