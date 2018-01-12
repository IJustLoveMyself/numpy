#************coding:utf-8****************
import numpy as np

# numpy - 统计函数
# numpy.amin() 沿指定轴返回最小值,相对应的元素比较，取最小值进行组合
# numpy.amax() 沿指定轴返回最大值,相对应的元素比较，取最大值进行组合

a = np.arange(12).reshape(2,2,3)
print a
# [[[ 0  1  2]
#   [ 3  4  5]]
#
#  [[ 6  7  8]
#   [ 9 10 11]]]
print np.amin(a,0)
# [[0 1 2]
#  [3 4 5]]
print np.amin(a,1)
# [[0 1 2]
#  [6 7 8]]
print np.amin(a,2)
# [[0 3]
#  [6 9]]
print np.amax(a,0)
# [[ 6  7  8]
#  [ 9 10 11]]
print np.amax(a,1)
# [[ 3  4  5]
#  [ 9 10 11]]
print np.amax(a,2)
# [[ 2  5]
#  [ 8 11]]
a = np.array([[[3,6,2],[ 12,9,5]],[[ 6 ,2, 8],[ 2,1,11]]])
print a
# [[[ 3  6  2]
#   [ 12 9  5]]
#
#  [[ 6  2  8]
#   [ 2  1 11]]]
print np.min(a,0)
# [[3 2 2]
#  [2 1 5]]
print np.min(a,1)
# [[3 6 2]
#  [2 1 8]]
print np.min(a,2)
# [[2 5]
#  [2 1]]
print np.max(a,0)
# [[ 6  6  8]
#  [12  9 11]]
print np.max(a,1)
# [[12  9  5]
#  [ 6  2 11]]
print np.max(a,2)
# [[ 6 12]
#  [ 8 11]]

# numpy.ptp()函数返回沿轴的值的范围(最大值减去最小值)
a = np.array([[[3,6,2],[ 12,9,5]],[[ 6 ,2, 8],[ 2,1,11]]])
print np.ptp(a,0)
# [[ 3  4  6]  np.max(a,0)减去np.min(a,0)
#  [10  8  6]]
print np.ptp(a,1)
# [[9 3 3]  np.max(a,1)减去np.min(a,1)
#  [4 1 3]]

# numpy.median()
# 中值定义为将数据样本的上半部分与下半部分分开的值
a = np.array([[30,65,70],[80,95,10],[50,90,60]])
print a
# [[30 65 70]
#  [80 95 10]
#  [50 90 60]]
print np.median(a) #将数组展开取中间值
# 65.0
print np.median(a, axis =  0) #沿0轴进行排序，取中间值
# [ 50.  90.  60.]
print np.median(a, axis =  1) #沿1轴进行排序，取中间值
#a  [ 65.  80.  60.]
a = np.arange(16).reshape(4,4)
print a
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
print np.median(a)
# 7.5 偶数则取中间两个数的平均值
print np.median(a,axis = 0)
# [ 6.  7.  8.  9.] 轴的长度为偶数时，取中间两个子数组元素对应位置的平均值
print np.median(a,axis = 1)
# [  1.5   5.5   9.5  13.5]

