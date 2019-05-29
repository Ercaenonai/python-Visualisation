# Matplotlib starting code
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Simple line plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show


#line plot with Title, x,y axis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5], [1,5,6,12,20])
plt.title('Test Plot', fontsize=30, color='g')
plt.xlabel('Python Mountain', fontsize=20, color='r')
plt.ylabel('A Slow Ascent', fontsize=15, color='b')
plt.show

#hire me plot
plt.figure(figsize=(2,5))
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0,6,0,20])
plt.annotate('You Should Hire ME!!!', (6,6), fontsize=20, color='r')
plt.show()


# bar graph
#plt.clf() Clears elements off figures
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Hire', 'Me', 'Please???', 'Thank you'), fontsize=15, color='b')
plt.bar(x,y, color=['lime', 'r', 'k','tan'])
plt.show()

#random dots 2 sets
d= {'Hire' : np.random.rand(10), 'ME' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro', 'gx'])
plt.show()

#time series
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180,3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

#random sized circles
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

#### df = pd.read_csv('CSV NAME.txt') uploading csv data to plot ##### Finaly!!!!

# multiple plots sharing same x axis
fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Share X')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x,y, color='r')
plots[1]. scatter(x, y)
plt.show()

#plt.savefig('name it'.png, jpg, tiff, pdf)<--- guessing you can save as all of those???