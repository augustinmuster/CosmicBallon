import numpy as np
import matplotlib.pyplot as plt

#------------------Mesures à 45 degrés--------------------
different_angle_mesurements=[9,10,11,12,13,14,15,16,17]
#---------------------------------------------------------

theFile=open("flight_data.txt", "r")

altitude=[]
altitude_error=[]
count_rate=[]
num=[]
i=0


for value in theFile.read().split():
    if(i==0):
        num.append(value)
    if(i==6):
        count_rate.append(value)
    if(i==10):
        altitude.append(value)
    if(i==11):
        altitude_error.append(value)
    if(i==21):
        i=-1

    i += 1

theFile.close()

print(num)
print(altitude)
print(altitude_error)
print(count_rate)

angle45_alt=[]
angle90_alt=[]
angle45_alt_error=[]
angle90_alt_error=[]

angle45_count=[]
angle90_count=[]
angle45_count_error=[]
angle90_count_error=[]

for i in range(1,len(num)):
    if int(num[i]) in different_angle_mesurements:
        angle45_alt.append(float(altitude[i]))
        angle45_count.append(float(count_rate[i]))
        angle45_count_error.append(np.sqrt(float(count_rate[i])))
        angle45_alt_error.append(float(altitude_error[i]))
    else:
        angle90_alt.append(float(altitude[i]))
        angle90_count.append(float(count_rate[i]))
        angle90_count_error.append(np.sqrt(float(count_rate[i])))
        angle90_alt_error.append(float(altitude_error[i]))


#plt.plot(angle45_alt,angle45_count, linestyle = 'none', marker = 'o', c = 'green',markersize = 2, label="zenith angle = 45°")
#plt.plot(angle90_alt,angle90_count, linestyle = 'none', marker = 'o', c = 'blue',markersize = 2, label="zenith angle= 90°")

plt.errorbar(angle45_alt, angle45_count, xerr=angle45_alt_error,yerr=angle45_count_error, fmt='o',c = 'green',markersize = 4,label="zenith angle = 45°")
plt.errorbar(angle90_alt, angle90_count, xerr=angle90_alt_error,yerr=angle90_count_error, fmt='o',c = 'blue',markersize = 4,label="zenith angle= 90°")
plt.title("Counts vs Altitude")
plt.xlabel("Mean Altitude (m)")
plt.ylabel("Counts / 10 minuts")

plt.legend()
plt.show()

