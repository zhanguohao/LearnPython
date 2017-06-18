# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x =np.array([1300,1400,1600,1900,2100,2300])
y = np.array([88000,72000,94000,86000,112000,98000])

z1 = np.polyfit(x,y,1)
p1 = np.poly1d(z1)
print p1
yvals = p1(x)

plot1 = plt.plot(x,yvals,'r')
plot2 = plt.plot(x,y,'bo')

plt.savefig('p3.png')
plt.show()