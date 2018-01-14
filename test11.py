#************coding:utf-8****************
import numpy as np

# 线性代数
# dot 两个数组的点积
# vdot 两个向量的点积
# inner 两个数组的内积
# matmul 两个数组的矩阵积
# determinant 数组的行列式
# solve 求解线性矩阵方程
# inv 寻找矩阵的乘法逆矩阵

# numpy.dot()
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print np.dot(a,b) #[[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
# [[37 40]
#  [85 92]]

# numpy.vdot()
# 此函数返回两个向量的点积
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print np.vdot(a,b) # 130  1*11 + 2*12 + 3*13 + 4*14 = 130
