#***********coding:utf-8***********
import numpy as np

#数组操作
#修改形状、展开
# reshape 不改变数据的条件下修改形状
# flat 数组上的一维迭代器
# flatten 返回展开为一维的数组副本
# ravel 返回连续的展开的一维数组

a = np.arange(6)
print a #[0 1 2 3 4 5]
b = a.reshape(2,3)
print b
# [[0 1 2]
#  [3 4 5]]

a = np.arange(8).reshape(2,4)
print a
# [[0 1 2 3]
#  [4 5 6 7]]
it=a.flat
print it #<numpy.flatiter object at 0x56254467b760> 返回的是一个一维迭代器
print it[5] #5
print it[4] #4
print it.next() #0

#ndarray.flatten(order)
#order：'C' — 按行，'F' — 按列，'A' — 原顺序，'k' — 元素在内存中的出现顺序。

a = np.arange(8).reshape(2,4)
print a
# [[0 1 2 3]
#  [4 5 6 7]]
print a.flatten()#[0 1 2 3 4 5 6 7]
print a.flatten("F")#[0 4 1 5 2 6 3 7]
a = np.array([[1,3,5,2],[3,4,9,8]])
print a.flatten("A")#[1 3 5 2 3 4 9 8]
print a.flatten("k")#[1 3 5 2 3 4 9 8]

#numpy.ravel(a, order)
a = np.arange(8).reshape(2,4)
print a
print a.ravel() #[0 1 2 3 4 5 6 7]
print a.ravel(order = "F") #[0 4 1 5 2 6 3 7]

######翻转操作#########################
# transpose 翻转数组的维度
# ndarray.T 和self.transpose()相同
# rollaxis 向后滚动指定的轴
# swapaxes 互换数组的两个轴

#numpy.transpose(arr, axes) arr:对应的数组  axes：对应的维度

a = np.arange(8).reshape(2,4)
print a
print a.transpose() #等价于np.transpose(a)
# [[0 4]
#  [1 5]
#  [2 6]
#  [3 7]]
print a.transpose([1,0])
#这个数组的shape是（2,4）,是二维的，维度编号可以是[0,1]，第一个维度是0,第二个维度是1,
# 翻转就是把第1维度和第2维度翻转， 所以是transpose([1,0])，如果是三维的话维度编号就是[0,1,2]
# [[0 4]
#  [1 5]
#  [2 6]
#  [3 7]]
a = np.arange(24).reshape(2,3,4)
print a
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

b = a.transpose([2,1,0])
print b
# [[[ 0 12]
#   [ 4 16]
#   [ 8 20]]
#
#  [[ 1 13]
#   [ 5 17]
#   [ 9 21]]
#
#  [[ 2 14]
#   [ 6 18]
#   [10 22]]
#
#  [[ 3 15]
#   [ 7 19]
#   [11 23]]]
print b.shape #(4, 3, 2) 维度1和维度3翻转，所以形状变成列（4,3,2）

b = a.transpose([1,0,2])
print b
# [[[ 0  1  2  3]
#   [12 13 14 15]]
#
#  [[ 4  5  6  7]
#   [16 17 18 19]]
#
#  [[ 8  9 10 11]
#   [20 21 22 23]]]
print b.shape #(3, 2, 4)

#numpy.ndarray.T
a = np.arange(8).reshape(2,4)