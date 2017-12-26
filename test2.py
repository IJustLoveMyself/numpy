#********coding:utf-8**********
import numpy as np

a = np.empty([2,3],dtype= int)#创建一个未初始化的数组，数组元素为随机值，因为它们未初始化
print a
# [[    140325788068776      94878459568640     140325746270496]
#  [    140325802735136 4412750543122677053 3556480777023654410]]
a = np.zeros([2,3])  #创建一个数组，以0填充
print a
#[[ 0.  0.  0.]
# [ 0.  0.  0.]]
a = np.ones([2,3])  #创建一个数组，以1填充
print a
#[[ 1.  1.  1.]
# [ 1.  1.  1.]]
a = np.array([[1,2,3],[4,5,6]])
b = np.zeros_like(a) #以a为模版创建数组b，并以0填充
c = np.ones_like(a) #以a为模版创建数组c，并以1填充
print b
#[[0 0 0]
# [0 0 0]]
print c
#[[1 1 1]
# [1 1 1]]
x = [(1,2,3),(4,5)]
a = np.array(x)
print a #[(1, 2, 3) (4, 5)]
print a.shape #(2,) 因为两个元组的个数不一样，所以列数无法确定，为空
#numpy.arange(start, stop, step, dtype)
# start:起始值默认为0
# stop：终止值，无默认值，需要指定
# step：步长，默认为1
a = np.arange(5)
print a #[0 1 2 3 4]
a = np.arange(3,14,2.6)
print a #[  3.    5.6   8.2  10.8  13.4]
#numpy.linspace（start, stop, num, endpoint, retstep, dtype）
#num：要生成的等间隔样例数量，即生成的数组中的元素的个数，默认为50
#endpoint 序列中是否包含stop值，默认为ture
#retstep 如果为true，返回样例，以及连续数字之间的步长
a = np.linspace(10,20,5)
print a #[ 10.   12.5  15.   17.5  20. ]
a = np.linspace(10,20,5,endpoint = False)
print a #[ 10.  12.  14.  16.  18.]
a = np.linspace(10,20,5,retstep = True)
print type(a) #返回的是元组<type 'tuple'>
print a #(array([ 10. ,  12.5,  15. ,  17.5,  20. ]), 2.5)
#numpy.logscale(start, stop, num, endpoint, base, dtype)
#start 起始值是base ** start
# stop 终止值是base ** stop
# num 范围内的数值数量，默认为50
# endpoint 如果为true，终止值包含在输出数组当中
# base 对数空间的底数，默认为10
a = np.logspace(1 , 10 , num = 10 , base = 2)
print a #[    2.     4.     8.    16.    32.    64.   128.   256.   512.  1024.]



