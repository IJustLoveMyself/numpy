#************coding:utf-8****************
import numpy as np


#算数函数

#三角函数
a = np.array([0,30,45,60,90])
# a*mp.pi/180 将其转化成弧度再进行计算
b = np.sin(a*np.pi/180)
print b
# [ 0.          0.5         0.70710678  0.8660254   1.        ]
c = np.cos(a*np.pi/180)
print c
# [  1.00000000e+00   8.66025404e-01   7.07106781e-01   5.00000000e-01
#    6.12323400e-17]
d = np.tan(a*np.pi/180)
print d
# [  0.00000000e+00   5.77350269e-01   1.00000000e+00   1.73205081e+00
#    1.63312394e+16]
#反三角函数
x = np.arcsin(b)
print x  # 得出的是弧度[ 0.          0.52359878  0.78539816  1.04719755  1.57079633]
print np.degrees(x) # 将弧度转化成角度[  0.  30.  45.  60.  90.]
x = np.arccos(c)
print x  # 得出的是弧度[ 0.          0.52359878  0.78539816  1.04719755  1.57079633]
print np.degrees(x) # 将弧度转化成角度[  0.  30.  45.  60.  90.]
x = np.arctan(d)
print x  # 得出的是弧度[ 0.          0.52359878  0.78539816  1.04719755  1.57079633]
print np.degrees(x) # 将弧度转化成角度[  0.  30.  45.  60.  90.]


#numpy.around(a,decimals)
#四舍五入到所需精度
#a 输入数组
#decimals 要舍入的小数位数。 默认值为0，保留到个位。 如果为负，整数将四舍五入到小数点左侧的位置。

a = np.array([1.1,5.55,  123,  0.567,  25.532])
print np.around(a)
# [   1.    6.  123.    1.   26.]
print np.around(a, decimals = 1)
# [   1.1    5.6  123.     0.6   25.5] 保留到小数点后1位
print np.around(a, decimals = 2)
# [   1.1     5.55  123.      0.57   25.53]保留到小数点后两位
print np.around(a, decimals = -1)
# [   0.   10.  120.    0.   30.] 保留到十位
print np.around(a, decimals = -2)
# [   0.    0.  100.    0.    0.]保留到百位


# numpy.floor()
# 此函数返回不大于输入参数的最大整数
a = np.array([-1.2,0.5,2.3,6])
print np.floor(a)
# [-2.  0.  2.  6.]