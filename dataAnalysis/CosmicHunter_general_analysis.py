# importation
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib as mpl
from matplotlib import gridspec
import numpy as np
##############################################DO NOT CHANGE THIS PART############################################
#------------------------fonctions-----------------
def map(min1,max1,min2,max2,value2):
    a= (max1-min1)/(max2-min2)
    b=min1-a*min2
    return a*value2+b
#--------------------------------------------------
theFile = open("data.txt", "r")

num = []
second = []
record_time = []
TOP = []
BOTTOM = []
ext = []
coincidence = []
altitude=[]

i = 0

ALT_INTERVALS=100
#insertion des données d'altitude (matrice temps,altitude, montée descente)
#temps auquel le palier d'altitude a été passée
time_alt_record=[0,4800,9000,12600,21000,23000]
alt_record=[1000,1100,1100,1200,1100,1000]
#insertion du numéro des mesures qui ont été prise à 45°
nonzero_angle=[3,12,20,29,31,37]
#----------------------------Lecture des données----------------cornicon gARNI à la Mezza !!!!!!!
for value in theFile.read().split():
    if (i >= 4 or i==0) :
        if(i==0): num.append(int(value))
        elif (i == 4) : second.append(int(value))
        elif (i == 5) : record_time.append(int(value))
        elif (i == 6) : TOP.append(int(value))
        elif (i == 7) : BOTTOM.append(int(value))
        elif (i == 8) : ext.append(int(value))
        elif (i == 9) :
            coincidence.append(int(value))
            i = -1
    i += 1
theFile.close()
#nombre de mesures
N_mesure=len(num)
#extraction de l'altitude de la mesure
alt=[]

for values in second:
    for j in range(1,len(time_alt_record)):
        if values>=time_alt_record[j-1] and values<time_alt_record[j]:
            alt.append(alt_record[j-1])

alt.append(alt_record[len(alt_record)-1])
#-----------------------------Affichage des données---------------------
print("---------------------\n")
print(num)
print("---------------------\n")
print(second)
print("---------------------\n")
print(record_time)
print("---------------------\n")
print(TOP)
print("---------------------\n")
print(BOTTOM)
print("---------------------\n")
print(ext)
print("---------------------\n")
print(coincidence)
print("---------------------\n")
print(alt)
#############################################################################################3
#calcul des valeurs moyennes
alt_only_one=[]
coincidence_alt_zero=[]
coincidence_alt_45=[]
for value in alt:
    if value not in alt_only_one:
        alt_only_one.append(value)
for value in alt_only_one:
    provisoire0=[]
    provisoire45=[]
    for j in range(0,len(num)):
        if alt[j]==value:
            if j in nonzero_angle:
                provisoire45.append(coincidence[j])
            else:
                provisoire0.append(coincidence[j])
    coincidence_alt_zero.append(provisoire0)
    coincidence_alt_45.append(provisoire45)

mean0=[]
mean45=[]

for value in coincidence_alt_45:
    mean45.append(np.mean(np.array(value)))
for value in coincidence_alt_zero:
    mean0.append(np.mean(np.array(value)))
#-----------------------------Histogrammes------------------------------
fig, (ax1,ax2)=plt.subplots(1,2)
#histogramme des valeurs moyennes à 0 degrés
alt_bar=[]
for value in alt_only_one:
    alt_bar.append(value+ALT_INTERVALS/2)
ax1.bar(alt_bar,mean0, width=ALT_INTERVALS,edgecolor='Black')
ax1.errorbar(alt_bar,mean0,yerr=np.std(np.array(mean0)),color='Grey')
ax1.set_xlabel('Altitude (m)')
ax1.set_ylabel('Mean numb of coincidences')
ax1.set_ylim(min(mean0)-20,max(mean0)+40)
ax1.set_xticks(np.arange(min(alt),max(alt)+ALT_INTERVALS+2,ALT_INTERVALS))
#ax1.set_yticks(np.arange(min(mean0)-20,max(mean0)+20,int((max(mean0)-min(mean0))/1.5)))
ax1.title.set_text('Mean number of particle counted with zenith angle=0')

#histogramme des valeurs moyennes à 45 degrés
ax2.bar(alt_bar,mean45, width=ALT_INTERVALS,edgecolor='Red')
ax2.errorbar(alt_bar,mean45,yerr=np.std(np.array(mean45)),color='Grey')
ax2.set_xlabel('Altitude (m)')
ax2.set_ylabel('Mean numb of coincidences')
ax2.set_ylim(min(mean0)-20,max(mean0)+40)
ax2.set_xticks(np.arange(min(alt),max(alt)+ALT_INTERVALS+2,ALT_INTERVALS))
#.set_yticks(np.arange(min(mean0)-20,max(mean0)+20,int((max(mean0)-min(mean0))/1.5)))
ax2.title.set_text('Mean number of particle counted with zenith angle=45')



fig.suptitle("Cosmic Hunter Mesurements, Mean value vs Altitude  ", fontsize=14)
plt.show()
