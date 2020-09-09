# importation
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib as mpl
from matplotlib import gridspec
import numpy as np

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
#insertion des données d'altitude (matrice temps,altitude, montée descente)
#temps auquel le palier d'altitude a été passée
time_alt_record=[0,4800,9000,12600,21000,23000]
alt_record=[1000,1100,1100,1200,1100,1000]
#insertion du numéro des mesures qui ont été prise à 45°
nonzero_angle=[3,12,20,29,31,37]
#----------------------------Lecture des données----------------
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
#-----------------------------Histogrammes------------------------------
fig=plt.figure(figsize=(15,5))
gs = gridspec.GridSpec(1, 2, width_ratios=[100, 5])
ax1=plt.subplot(gs[0])
ax3=plt.subplot(gs[1])

#ax2=plt.subplot()
#histogramme principal
couleur = []
Blues = plt.get_cmap('Blues')
for value in alt:
    couleur.append(Blues(map(0,1,min(alt),max(alt),value)))

couleur_bordure=[]
for value in num:
    if value in nonzero_angle:
        couleur_bordure.append("red")
    else:
        couleur_bordure.append("black")

graph=ax1.bar(num,coincidence,color=couleur,edgecolor=couleur_bordure)
ax1.set_xlabel('Mesure number')
ax1.set_ylabel('Particle counted')
ax1.set_ylim(min(coincidence)-10,max(coincidence)+10)
ax1.set_xticks(np.arange(0,N_mesure,10))
ax1.set_yticks(np.arange(min(coincidence),max(coincidence),20))
ax1.title.set_text('Flight overwiew')

legend_elements = [Line2D([0], [0], color='Black', label='zenith angle=0°'),
                   Line2D([0], [0], color='Red', label='zenith angle=45°')]
ax1.legend(handles=legend_elements)

cmap = mpl.cm.Blues
norm = mpl.colors.Normalize(vmin=min(alt), vmax=max(alt))

cb1 = mpl.colorbar.ColorbarBase(ax3, cmap=cmap,
                                norm=norm,
                                orientation='vertical')
ax3.set_ylabel('Altitude(m)')

fig.suptitle("Cosmic Hunter Mesurements, Flight Overview  ", fontsize=14)
plt.show()
