import matplotlib.pyplot as plt

theFile=open("flight_data.txt", "r")

int_p=[]
int_t=[]
int_h=[]
ext_p=[]
ext_t=[]
ext_h=[]
alt=[]
time=[]

i=0
key=0

for value in theFile.read().split():
    if(i==1):
        if(key==1):
            time.append(float(value)/60)
    if(i==7):
        if(key==1):
            int_p.append(float(value))
    if(i==8):
        if(key==1):
            int_t.append(float(value))
    if(i==9):
        if(key==1):
            int_h.append(float(value))
    if(i==10):
        if(key==1):
            alt.append(float(value))
    if(i==16):
        if(key==1):
            ext_t.append(float(value))
    if(i==18):
        if(key==1):
            ext_p.append(float(value))
    if(i==20):
        if(key==1):
            ext_h.append(float(value))
    if(i==21):
        if(key==0):
            key=1
        i=-1

    i += 1

theFile.close()

print(int_h)
print(int_t)
print(int_p)
print(alt)

print(ext_h)
print(ext_t)
print(ext_p)
print(time)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True)
fig.suptitle('Flight Environnment Parameters')

ax1.plot(time, alt, color="red")
ax1.set_ylabel("Altitude(m)")


ax2.plot(time,int_t, color="magenta", label="Inside the box")
ax2.plot(time,ext_t, color="purple", label="Outside the box")
ax2.set_ylabel("Temperature(°C)")

ax3.plot(time,int_p, color="darkblue", label="Inside the box")
ax3.plot(time,ext_p, color="dodgerblue", label="Outside the box")
ax3.set_ylabel("Pressure (mm Hg)")

ax4.plot(time,int_h, color="green", label="Inside the box")
ax4.plot(time,ext_h, color="springgreen", label="Outside the box")
ax4.set_ylabel("Humidity (%)")


plt.xlabel("Time (min)")

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()

plt.show()