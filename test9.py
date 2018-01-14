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

# numpy.mean()
# 算术平均值是沿轴的元素的总和除以元素的数量。 numpy.mean()函数返回数组中元素的算术平均值
a = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]]])
print a
# [[[1 1 1]
#   [2 2 2]]
#
#  [[3 3 3]
#   [4 4 4]]]
print np.mean(a) #2.5 没有指定轴，把数组展开计算平均值
print np.mean(a,0) #沿轴0计算平均值 即（a[axis,x1,y1]+a[axis,x2,y2]）/2  x1=x2 y1=y2这里总共有6个
# [[ 2.  2.  2.]
#  [ 3.  3.  3.]]
print np.mean(a,1) #沿轴1计算平均值 即（a[x1,axis,y1]+a[x2,axis,y2]）/2  x1=x2 y1=y2这里总共有6个
# [[ 1.5  1.5  1.5]
#  [ 3.5  3.5  3.5]]
print np.mean(a,2) #沿轴2计算平均值 即（a[x1,y1,axis]+a[x2,y2,axis]）/2  x1=x2 y1=y2这里总共有4个
# [[ 1.  2.]
#  [ 3.  4.]]

# numpy.average()
# 加权平均值是由每个分量乘以反映其重要性的因子得到的平均值。
# numpy.average()函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。
# 该函数可以接受一个轴参数。 如果没有指定轴，则数组会被展开。
# 加权平均值 = (x1*w1+x2*w2+x3*w3+...+xk*wk)/(w1+w2+w3+...+w4)
# 不指定权重时相当于 mean 函数
# 如果 returned 参数设为 true，则返回权重的和
#权重的形状要和数组的形状相同，如果指定了轴，则权重的形状可以不和数组的形状相同，可以只和轴的形状相同
a = np.arange(6).reshape(3,2)
wt = np.array([[3,5],[3,4],[3,5]])
print np.average(a) # 2.5平均值
print np.average(a, weights = wt)
# 2.60869565217 没有指定轴
print np.average(a, axis = 1, weights = wt, returned =  True)
# (array([ 0.625     ,  2.57142857,  4.625     ]), array([ 8.,  7.,  8.]))
# 指定了轴1,计算的时候轴1的坐标在变，其他轴的坐标不变，返回权重之和
wt = np.array([2,2])
print np.average(a, axis = 1, weights = wt, returned =  True)
# (array([ 0.5,  2.5,  4.5]), array([ 4.,  4.,  4.]))

# 标准差
# 标准差是与均值的偏差的平方的平均值的平方根
# numpy.std
a = np.arange(4)
print np.std(a) #1.11803398875

# 方差
# 标准差是方差的平方根
# numpy.var
a = np.arange(4)
print np.var(a)
# 1.25


