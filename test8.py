#************coding:utf-8****************
import numpy as np

# NumPy - 算数运算
# 输入数组必须具有相同的形状或符合数组广播规则,元素运算，对应位置的元素进行运算
# add() 加
# subtract() 减
# multiply() 乘
# divide() 除

a = np.arange(9).reshape(3,3)
b = np.array([1,2,3], dtype = np.float64)
print np.add(a,b)
# [[  1.   3.   5.]
#  [  4.   6.   8.]
#  [  7.   9.  11.]]
print np.subtract(a,b)
# [[-1. -1. -1.]
#  [ 2.  2.  2.]
#  [ 5.  5.  5.]]
print np.multiply(a,b)
# [[  0.   2.   6.]
#  [  3.   8.  15.]
#  [  6.  14.  24.]]
print np.divide(a,b)
# [[ 0.          0.5         0.66666667]
#  [ 3.          2.          1.66666667]
#  [ 6.          3.5         2.66666667]]

# numpy.reciprocal()
# 函数返回参数逐元素的倒数
# 对0取倒数会出现警告 RuntimeWarning: divide by zero encountered in reciprocal
a = np.array([0.25,  1.33,  1,   100])
print np.reciprocal(a)
# [ 4.         0.7518797  1.         0.01     ]
print type(a[3]) # <type 'numpy.float64'>
a = np.arange(1,10)
print np.reciprocal(a)
# [1 0 0 0 0 0 0 0 0] 因为a中的元素都是整型的，所以得到的结果也是整型的，所以数组中大于整数的倒数是0

# numpy.power()
# 此函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂
a = np.arange(1,5)
b = np.array([2,2,2,2])
print np.power(a,b) #[ 1  4  9 16]

# numpy.mod()
# numpy.remainder()
# 返回输入数组中相应元素的除法余数
a = np.array([10,5,11,17])
b = np.array([3,2,5,5])
print np.mod(a,b) # [1 1 1 2]
print np.remainder(a,b) # [1 1 1 2]

