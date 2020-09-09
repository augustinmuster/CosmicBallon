import matplotlib.pyplot as plt

#------------------Mesures à 45 degrés--------------------
different_angle_mesurements=[2]
#---------------------------------------------------------

theFile=open("flight_data.txt", "r")

latitude=[]
longitude=[]
i=0


for value in theFile.read().split():
    if(i==14):
        longitude.append(value)
    if(i==12):
        latitude.append(value)
    if(i==21):
        i=-1

    i += 1

theFile.close()

print(latitude)
print(longitude)

lat=[]
long=[]

for i in range (1,len(latitude)):
    lat.append(float(latitude[i]))
    long.append(float(longitude[i]))

print(lat)
print(long)

BBox = [6.9550,  7.3512, 46.7022, 46.8790]

#ruh_m=plt.imread('fribourg.PNG')


fig, ax = plt.subplots(figsize = (8,7))
ax.set_title('Plotting Spatial Data on Riyadh Map')
#ax.set_xlim(BBox[0],BBox[1])
#ax.set_ylim(BBox[2],BBox[3])
#ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
ax.scatter(lat, long)
plt.show()