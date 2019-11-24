# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 01:28:21 2019

@author: rubag
"""
''' Matplotlib library '''

import matplotlib.pyplot as plt

''' 1) 
        Plotting Line Charts '''        

from matplotlib import style
style.use('ggplot') # To import special looking charts
print(style.available) # Prints all available graph styles
style.use('grayscale')

plt.plot(range(10), [2, 4.5, 1, 2, 3.5, 2, 1, 2, 3, 2])
plt.title("Line Chart")
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Plotting Multiple charts in a single plot
plt.plot(range(10), [2, 4.5, 1, 2, 3.5, 2, 1, 2, 3, 2], label='jim') # graph 1 with legends
plt.plot(range(10), [3, 4, 2, 5, 2, 4, 2.5, 4, 3.5, 3], label='tom') # graph 2 with legends
plt.title("Line Chart")
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend() # To show legends

''' 2) 
        Plotting Bar Charts '''        

plt.bar(range(10), [2, 4.5, 1, 2, 3.5, 2, 1, 2, 3, 2], label='jim', color='m', align='center', alpha=0.5)
# Aplha to make the bars translucent
plt.bar(range(10), [3, 4, 2, 5, 2, 4, 2.5, 4, 3.5, 3], label='tom', color='g', align='center', alpha=0.5)
plt.title("Line Chart")
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.grid(True)

rainfall = [17, 9, 16, 3, 21, 7, 8, 4, 6, 21, 4, 1]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.bar(months, rainfall, align='center', color='y') 
plt.xticks(months,rotation='vertical')
plt.xlabel('Months')
plt.ylabel('Rainfall')
plt.title('Raninfall in different months for the year 19995')
plt.grid(True)
plt.savefig('Bar_graph.png', bbox_inches='tight')
# Saving the graph 'bbox_inches='tight'' removes the extra white spaces

plt.plot([1, 2, 3, 4], [1, 8, 27, 64], 'bo') # Blue circle marker
plt.axis([0, 4.5, 0, 70]) # xmin, xmax, ymin, ymax

import numpy as np
a = np.arange(1, 4.5, 0.1)
plt.plot(a, a**2, 'y^') # Yellow triangle marker
plt.plot(a, a**3, 'r--') # Red dashed marker

plt.subplot(121) # 1 row, 2 col, chart 1 --OR-- plt.subplot(121)
plt.plot([1, 2, 3, 4], [1, 8, 27, 125], 'y^')
plt.subplot(122) # 1 row, 2 col, chart 2
plt.plot(a, a**2, 'bo', a, a**3, 'r--', a, a**4, 'b^')
plt.axis([0, 4.5, 0, 70]) 

