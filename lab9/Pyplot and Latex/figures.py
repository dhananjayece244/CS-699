import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.random import normal


#reading csv file.
df = pd.read_csv('input.csv')
data = df['2003-04'].head(20)
data1 = df['2007-08'].head(20)

#Data for line graph.
side_length = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
area = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0]

#line graph 
plt.plot(side_length, area, label='Square')
plt.xlabel('Side')
plt.ylabel('Area')
plt.title('Area of Shapes')
plt.legend()
plt.savefig('image1.pdf')

#bar chart
plt.figure(3)
data.plot(kind='bar')
plt.xlabel('Sector')
plt.ylabel('FDI')
plt.title('Bar chart')
plt.savefig('image2.pdf')

#Histogram chart
plt.figure(2)
gaussian_numbers = normal(size=1000)
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig('image3.pdf')

#red circled dot graph.
plt.figure(6)
x= [1,2,3,4,5]
y= [3,5,7,8,10]
plt.plot(x, y, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('image4.pdf')


#Generate table.tex
df = pd.DataFrame(np.random.random((4,5)))
file = open('table.tex','w')
file.write(df.to_latex())
file.close()

