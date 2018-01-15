#***********coding:utf-8***********
import numpy as np

# numpy.broadcast_to(array, shape, subok)
# 此函数将数组广播到新形状,遵守广播兼容的原则

a = np.arange(3).reshape(1,3)
print a
# [[0 1 2]]
b = np.broadcast_to(a,(3,3))
print b
# [[0 1 2]
#  [0 1 2]
#  [0 1 2]]

# numpy.expand_dims(arr, axis)
# 函数通过在指定位置插入新的轴来扩展数组形状
# arr：输入数组
# axis：新轴插入的位置

a = np.arange(8).reshape(4,2)
print a
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]]
print a.shape #(4, 2)
print a[1,0]
b = np.expand_dims(a,0) #a有两个轴0,1.现在在a的0轴的位置增加一个长度为1的0轴,
# 在a中2的位置是a[1,0],在b中2的位置就变成了b[0,1,0]
print b
# [[[0 1]
#   [2 3]
#   [4 5]
#   [6 7]]]
print b.shape #(1, 4, 2)
c = np.expand_dims(a,1) #在1轴的位置增加了一个长度为1的轴，此时2的位置是c[1,0,0]
print c
# [[[0 1]]
#
#  [[2 3]]
#
#  [[4 5]]
#
#  [[6 7]]]
print c.shape #(4, 1, 2)

# numpy.squeeze(arr, axis)
# 函数从给定数组的形状中删除长度为1的轴
# arr：输入数组
# axis：整数或整数元组，用于选择形状中单一维度条目的子集

a = np.arange(8).reshape(1,4,2)
print a
# [[[0 1]
#   [2 3]
#   [4 5]
#   [6 7]]]
print a.shape #(1, 4, 2)
print a[0,1,0] #2
b = np.squeeze(a,0)
print b
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]]
print b.shape #(4, 2)
print b[1,0] #2 删除列a中的0轴

# 数组的连接
# numpy.concatenate((a1, a2, ...), axis)
# 此函数用于沿指定轴连接相同形状的两个或多个数组
# a1, a2, ...：相同类型的数组序列,形状相同（轴长相同）
# axis：沿着它连接数组的轴，默认为 0

a = np.arange(4).reshape(2,2)
b = np.arange(5,9).reshape(2,2)
c = np.concatenate((a,b),0)
print c
# [[0 1]
#  [2 3]
#  [5 6]
#  [7 8]]
c = np.concatenate((a,b),1)
print c
# [[0 1 5 6]
#  [2 3 7 8]]

# numpy.stack(arrays, axis)
# 此函数沿新轴连接数组序列
# arrays：相同形状的数组序列
# axis：返回数组中的轴，输入数组沿着它来堆叠

a = np.arange(4).reshape(2,2)
b = np.arange(5,9).reshape(2,2)
c = np.stack((a,b),0)
print c #在a和b中0轴的位置增加一个长度为1的轴，在a中该新增轴的位置的值是0则2的位置从a[1,0]变成列a[0,1,0],
# 在b中该轴的位置的值是1则5的位置从b[0,0]变成了b[1,0,0].剩下的以此类推
# [[[0 1]
#   [2 3]]
#
#  [[5 6]
#   [7 8]]]
c = np.stack((a,b),1)
print c # 在a和b中1轴的位置增加一个长度为1的轴，在a中该新增轴的位置的值是0则2的位置从a[1,0]变成列a[1,0,0],
# 在b中该轴的位置的值是1则5的位置从b[0,0]变成了b[0,1,0].剩下的以此类推
# [[[0 1]
#   [5 6]]
#
#  [[2 3]
#   [7 8]]]

# numpy.hstack
# 通过水平堆叠来生成水平的单个数组
a = np.arange(4).reshape(2,2)
b = np.arange(5,9).reshape(2,2)
c = np.hstack((a,b))
print c
# [[0 1 5 6]
#  [2 3 7 8]]

# numpy.vstack
# 通过竖直堆叠来生成竖直的单个数组
a = np.arange(4).reshape(2,2)
b = np.arange(5,9).reshape(2,2)
c = np.vstack((a,b))
print c
# [[0 1]
#  [2 3]
#  [5 6]
#  [7 8]]

# numpy.split(ary, indices_or_sections, axis)
# 该函数沿特定的轴将数组分割为子数组
# ary:输入的数组
# indices_or_sections：要平均分成几份
# axis：要沿哪个轴分割，默认是0
a = np.arange(6).reshape(3,2)
print a
# [[0 1]
#  [2 3]
#  [4 5]]
b = np.split(a,3,0) #沿轴0分割成3份，轴长必须是要分割份数的整数倍
print b
# [array([[0, 1]]), array([[2, 3]]), array([[4, 5]])]
b = np.split(a,2,1) #沿轴1分割成2份，轴长必须是要分割份数的整数倍
print b
# [array([[0],
#        [2],
#        [4]]), array([[1],
#        [3],
#        [5]])]

# numpy.hsplit 可以理解为axis=1的numpy.split的特殊形式。
a = np.arange(6).reshape(3,2)
print a
b = np.hsplit(a,2)
print b
# [array([[0],
#        [2],
#        [4]]), array([[1],
#        [3],
#        [5]])]

# numpy.vsplit 可以理解为axis=0的numpy.split的特殊形式。
a = np.arange(6).reshape(3,2)
print a
b = np.vsplit(a,3)
print b
# [array([[0, 1]]), array([[2, 3]]), array([[4, 5]])]

# 添加/删除元素
# resize 返回指定形状的新数组
# append 将值添加到数组末尾
# insert 沿指定轴将值插入到指定下标之前
# delete 返回删掉某个轴的子数组的新数组
# unique 寻找数组内的唯一元素

#numpy.resize(arr, shape)
# 此函数返回指定大小的新数组。 如果新大小大于原始大小，则包含原始数组中的元素的重复元素
# 等于是把数组展开成一维，然后重新定义形状，多余的不要，不够的重复进行填充
a = np.arange(6).reshape(2,3)
print a
# [[0 1 2]
#  [3 4 5]]
b = np.resize(a,(3,2))
print b
# [[0 1]
#  [2 3]
#  [4 5]]
c = np.resize(a,(4,2)) #不够的情况
print c
# [[0 1]
#  [2 3]
#  [4 5]
#  [0 1]]
d = np.resize(a,(2,2)) #多余的情况
print d
# [[0 1]
#  [2 3]]

# numpy.append(arr, values, axis)
# 此函数在输入数组的末尾添加值
# arr：输入数组
# values：要向arr添加的值，比如和arr形状相同(除了要添加的轴)
# axis：沿着它完成操作的轴。如果没有提供，arr和values两个参数都会被展开成一维数组

a = np.arange(6).reshape(2,3)
b = np.append(a,[[7,8,9]])
print b #[0 1 2 3 4 5 7 8 9] 没有提供参数axis，所以倍展开成一维数组
c = np.append(a,[[7,8,9]],0)
print c #沿0轴添加，添加的数组对应的0轴的轴长要相等
# [[0 1 2]
#  [3 4 5]
#  [7 8 9]]
d = np.append(a,[[7],[8]],1)
print d
# [[0 1 2 7]
#  [3 4 5 8]]

# numpy.insert(arr, obj, values, axis)
# 此函数在给定索引之前，沿给定轴在输入数组中插入值
# arr：输入数组
# obj：在其之前插入值的索引
# values：要插入的值，需要和原数组对应要插入的轴长相同或者可以进行广播兼容
# axis：沿着它插入的轴，如果未提供，则输入数组会被展开

a = np.array([[1,2],[3,4],[5,6]])
print a
print np.insert(a,3,[11,12]) #未传递 axis 参数。 在插入之前输入数组会被展开
# [ 1  2  3 11 12  4  5  6]
print np.insert(a,1,[11],axis = 0)
#传递了 axis 参数。 会0轴广播值数组来配输入数组。，索引的值是0轴的索引值。
# [[ 1  2]
#  [11 11]
#  [ 3  4]
#  [ 5  6]]
print np.insert(a,1,[11],axis = 1)
#传递了 axis 参数。 会0轴广播值数组来配输入数组。，索引的值是0轴的索引值。
# [[ 1 11  2]
#  [ 3 11  4]
#  [ 5 11  6]]

# numpy.delete(arr, obj, axis)
# 函数返回从输入数组中删除指定子数组的新数组
# arr：输入数组
# obj：要删除的值的索引值
# axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开

a = np.arange(12).reshape(3,4)
b = np.delete(a,4)
print b #[ 0  1  2  3  5  6  7  8  9 10 11] 没有提供axis的值数组被展开，删除列索引4处的值
c = np.delete(a,1,0) #删除0轴上索引值为1的元素
print c
# [[ 0  1  2  3]
#  [ 8  9 10 11]]
d = np.delete(a,1,1) #删除1轴上索引值为1的元素
print d
# [[ 0  2  3]
#  [ 4  6  7]
#  [ 8 10 11]]

#numpy.unique(arr, return_index, return_inverse, return_counts)
# 返回输入数组中的去重元素数组
# arr：输入数组，如果不是一维数组则会展开
# return_index：如果为true，返回输入数组中的元素下标
# return_inverse：如果为true，返回去重数组的下标，它可以用于重构输入数组
# return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数

a = np.array([[1,2,3,2,2,4,5,3,2,5,5,2,]])
b,c,d,e = np.unique(a,True,True,True)
print b #[1 2 3 4 5] 去重后的数组
print c #[0 1 2 5 6] 去重后的数组的元素在原数组中的下标
print d #[0 1 2 1 1 3 4 2 1 4 4 1] 原数组中的元素在去重后的数组中的对应的下表
print e #[1 5 2 1 3] 去重后的数组的元素在原书组中对应出现的次数
