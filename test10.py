#************coding:utf-8****************
import numpy as np

# numpy.sort()
# sort()函数返回输入数组的排序副本
# a 要排序的数组
# axis 沿着它排序数组的轴，如果没有指定则沿着最后的轴排序
# kind 默认为'quicksort'(快速排序)'quicksort'(快速排序)	'mergesort'(归并排序)	'heapsort'(堆排序)
# order 如果数组包含字符串，则是要排序的字符串
a = np.array([[3,6,2],[5,7,1]])
print np.sort(a)
# [[2 3 6]
#  [1 5 7]] 没有指定轴，因为轴1是最后的轴，则沿轴1进行排序
print np.sort(a,axis=1)
# [[2 3 6]
#  [1 5 7]]
dt = np.dtype([('name',  'S4'),('age',  int)]) # 自定义数据类型，S4表示长度为4的字符串
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)
print np.sort(a, order =  'name')
# [('amar', 27) ('anil', 25) ('raju', 21) ('ravi', 17)]

# numpy.argsort()
# 函数对输入数组沿给定轴执行排序，返回排序后原数组的索引
a = np.array([4,  1,  3])
print np.argsort(a) #[1 2 0]
a = np.array([[[14,5,2],[7,13,4]],[[11,2,9],[1,8,12]]])
print np.argsort(a)
# [[[2 1 0]
#   [2 0 1]]
#
#  [[1 2 0]
#   [0 1 2]]] 没有指定轴，默认沿轴2进行排序
print np.argsort(a,2)
# [[[2 1 0]
#   [2 0 1]]
#
#  [[1 2 0]
#   [0 1 2]]]
print np.argsort(a,0)
# [[[1 1 0]
#   [1 1 0]]
#
#  [[0 0 1]
#   [0 0 1]]] 沿0轴进行排序


# numpy.argmax() 返回指定轴的最大值的索引
# numpy.argmin() 返回指定轴的最小值的索引
# 如果没有指定轴，则将数组展开，找最大或最小值，返回索引
a = np.array([[[14,5,2],[7,13,4]],[[11,2,9],[3,8,15]]])
print np.argmax(a) #11 没有指定轴，则展开数组
print np.argmin(a) #2
print np.argmax(a,0)
# [[0 0 1]
#  [0 0 1]]
print np.argmin(a,0)
# [[1 1 0]
#  [1 1 0]]
print np.argmax(a,2)
# [[0 1]
#  [0 2]]
print np.argmin(a,2)
# [[2 2]
#  [1 0]] 沿2轴比较，返回最小值索引

# numpy.nonzero()
# 函数返回输入数组中非零元素的索引。
a = np.array([[[0,5,2],[7,13,1]],[[1,2,9],[1,1,15]]])
print np.nonzero(a)
# array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]),
# array([0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]),
# array([1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2])
#返回值从上到下分别代表轴0、轴1、轴2上的索引

# numpy.where()
# 返回输入数组中满足给定条件的元素的索引
a = np.array([[[0,5,2],[7,13,1]],[[1,2,9],[1,1,15]]])
print np.where(a == 0) #(array([0]), array([0]), array([0]))
print np.where(a>10) #(array([0, 1]), array([1, 1]), array([1, 2]))

# numpy.extract()
# 函数返回任何满足条件的元素
a = np.array([[[0,5,2],[7,13,1]],[[1,2,9],[1,1,15]]])
condtion = np.mod(a,2) == 0
print condtion #定义条件，condtion只是一个普通的变量，可以随便定义。
# [[[ True False  True]
#   [False False False]]
#
#  [[False  True False]
#   [False False False]]]
print np.extract(condtion, a)
# [0 2 2] 返回满足条件的元素

