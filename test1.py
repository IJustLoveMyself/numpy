#************coding:utf-8****************
import numpy as np

#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
#object：可以是列表，可以是元组
#dtype 数组的所需数据类型，可选
#copy 可选，默认为true，对象是否被复制
#order C(按行)、F(按列)或A(任意，默认)
#subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
#ndimin 指定返回数组的最小维数。
a = np.array([[[1, 2, 3], [4, 5, 6]],
              [[1,2,3],[4,5,6]]])   #用列表创建数组
print a
#[[[1 2 3]
#  [4 5 6]]
# [[1 2 3]
#  [4 5 6]]]
print a.shape  # (2, 2, 3) #数组的形状
print a[:,:,2]   #获取其中的元素
# [[3 6]
#  [3 6]]
print type(a[:,:,2]) #<type 'numpy.ndarray'>  获取结果的类型
print a.size  #12  数组的大小（长度）
print a.ndim  #3  数组的维数 三维a[:,:,:]

a = np.array(((2,3),(2,3))) #用元组来创建数组
print a
#[[2 3]
# [2 3]]

b = np.array([[1,2,3],[4,5,6]])
print b
#[[1 2 3]
# [4 5 6]]
print b.shape #(2, 3)
print b[1,2]  # 6
print type(b[1,2]) #<type 'numpy.int64'>
print b.size  # 6
print b.ndim  #2 数组的维数 二维 b[:,:]

c = np.array([[1,2],[4,5],[7,8]])
print c
#[[1 2]
# [4 5]
# [7 8]]
print c.shape #(3,2)
print c[:,1] #[2 5 8]
print type(c[:,1]) #<type 'numpy.ndarray'>
print c.size #6
print c.ndim #2 数组的维数 二维 c[:,:]
