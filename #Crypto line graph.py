#Crypto line graph
import matplotlib.pyplot as plt

x = [1,2,3,4] 
y = [5,7,4,2]

x2 = [1,2,3,4]
y2 = [6,10,1,.05]

plt.plot(x, y, label='Crypto Mkt. Cap')
plt.plot(x2, y2, label= "Hope")
plt.xlabel('Time Frame')
plt.ylabel('Crypto portfolio value')

plt.title('Crypto Portfolio\nOooops')
plt.legend()
plt.show()



#Volatile Organic Compounds Bar
x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 =[1,3,5,7,9]
y2 =[5,3,6,7,5]

plt.bar(x, y, label='Diflormethylbromine', color='b')
plt.bar(x2, y2, label='Tetrachloralethelene', color='c')

plt.xlabel('Well ID')
plt.ylabel('Volatile Organic Compounds')

plt.title('VOC"s\nPer Well')
plt.legend()
plt.show()

#Histogram
voc_over_time = [22,55,44,35,90,25,10,5,34,78,86,46,21,12]

#id = [x forx in range(len(population_ages))]

bins = [0,10,20,40,50,60,70,80,90,100]

plt.hist(voc_over_time, bins, histtype='bar', rwidth=0.8)

plt.xlabel('VOC"s over Time')
plt.ylabel('Concentrations')

#Scatter plot with line
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,3,6,7,8,8,5,3]

plt.scatter(x,y, label='Scatter', color='g', marker='2', s=250)
plt.plot(x, y, label='Line', color='r')
plt.xlabel ('x')
plt.ylabel ('y')
plt.title ('Scatter Plot\nScatter Data')
plt.legend()

#StackPlot

import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,6,8,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,3]
playing = [8,5,7,13,4]

plt.stackplot(days, sleeping,eating,working,playing)

plt.plot([],[],color='r', label='Sleeping', linewidth=5)
plt.plot([],[],color='g', label='Eating', linewidth=5)
plt.plot([],[],color='orange', label='Working', linewidth=5)
plt.plot([],[],color='b', label='Playing', linewidth=5)

plt.xlabel('Days')
plt.ylabel('Hours per Day')
plt.title('Stack Plot\nHours per Activity')
plt.legend()
plt.plot()
