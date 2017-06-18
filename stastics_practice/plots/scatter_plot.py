# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1700,2100,1900,1300,1600,2200],[51000,63000,57000,39000,48000,66000],'ro')
x = np.array([1700, 2100, 1900, 1300, 1600, 2200])
y = np.array([53000, 65000, 59000, 41000, 50000, 68000])
print x
print y

for (x1, y1) in zip(x, y):
    print y1 / x1

z1 = np.polyfit(x, y, 1)

p1 = np.poly1d(z1)
print z1
print p1
yvals = p1(x)
plot1 = plt.plot(x, y, 'go', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('polyfitting')

# fg = plt.gcf()
# plt.show()
# fg.savefig('p1.png')

plt.savefig('p2.png', dpi=200)
plt.show()

'''
    保存成图片的时候，是空白的图片，解决方法：
        不过，方法1的分辨率低，可以通过参数设置
    （1）：展示之前调用：
        plt.savefig("filename.png")
        plt.show()
    （2）：先保存起来：
        # gcf: Get Current Figure
        fig = plt.gcf()
        plt.show()
        fig1.savefig('tessstttyyy.png', dpi=100)
'''


# plt.plot([1700,2100,1900,1300,1600,2200],[53000,65000,59000,41000,50000,68000],'ro')

# plt.xlabel('size')
# plt.ylabel('price')
# plt.title('house price')
# plt.show()
