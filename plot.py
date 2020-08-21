import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('bb_in_air.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=",")
    for row in plots:
        x.append(row[0])
        y.append(row[2])

plt.plot(x,y, marker='o')

plt.title('....')

plt.xlabel('...')
plt.ylabel('...')

plt.show()
#
