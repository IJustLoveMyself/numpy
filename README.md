numpy

####################################

http://www.yiibai.com/numpy/

####################################


dtype_test.py

对numpy中dtype进行了简单介绍


test1.py

通过例子描述了numpy.arrary的一些特性


test2.py

数组的创建

numpy.empty 生成未初始化的数组

numpy.ones  生成初始化为1的数组

numpy.zeros 生成初始化为0的数组

numpy.arange

numpy.linespace

numpy.logspace


test3.py

数组的分割、过滤


test4.py

对数组的广播的理解


test5.py

numpy.reshape 不改变数据的条件下修改形状

numpy.flat 返回数组上的一维迭代器

numpy.flatten 返回展开为一维的数组副本

numpy.ravel 返回连续的展开的一维数组

numpy.transpose 翻转数组的维度

numpy.ndarray.T 和self.transpose()相同

numpy.rollaxis 向后滚动指定的轴

numpy.swapaxes 互换数组的两个轴


test6.py

numpy.broadcast_to 函数将数组广播到新形状,遵守广播兼容的原则

numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状

numpy.squeeze 函数从给定数组的形状中删除长度为1的轴

numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组

numpy.stack 函数沿新轴连接数组序列

numpy.hstack 通过水平堆叠来生成水平的单个数组

numpy.vstack 通过竖直堆叠来生成竖直的单个数组

numpy.split 函数沿特定的轴将数组分割为子数组

numpy.hsplit 可以理解为axis=1的numpy.split的特殊形式

numpy.vsplit 可以理解为axis=0的numpy.split的特殊形式

numpy.resize 此函数返回指定大小的新数组

numpy.append 此函数在输入数组的末尾添加值

numpy.insert 此函数在给定索引之前，沿给定轴在输入数组中插入值

numpy.delete 函数返回从输入数组中删除指定子数组的新数组

numpy.unique 返回输入数组中的去重元素数组


test7.py

三角函数：

numpy.sin

numpy.cos

numpy.tan

反三角函数：

numpy.arcsin

numpy.arccos

numpy.arctan

numpu.degrees 将弧度转化成度

numpy.pi 派

numpy.around 对数组中元素进行四舍五入

numpy.floor 此函数返回不大于输入参数的最大整数


test8.py

numpy.add 加

numpy.subtract 减

numpy.multiply 乘

numpy.divide 除

numpy.reciprocal 函数返回参数逐元素的倒数

numpy.power 此函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂

numpy.mod 返回输入数组中相应元素的除法余数

numpy.remainder 返回输入数组中相应元素的除法余数


test9.py

numpy.amin 沿指定轴返回最小值,相对应的元素比较，取最小值进行组合

numpy.amax 沿指定轴返回最大值,相对应的元素比较，取最大值进行组合

numpy.ptp 函数返回沿轴的值的范围(最大值减去最小值)

numpy.median 返回数组的中值,中值定义为将数据样本的上半部分与下半部分分开的值

numpy.mean 返回算数平均值,算术平均值是沿轴的元素的总和除以元素的数量

numpy.average 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值

numpy.std 求标准差,标准差是与均值的偏差的平方的平均值的平方根

numpy.var 求方差,标准差是方差的平方根


test10.py

numpy.sort 函数返回输入数组的排序副本，默认从小到大

numpy.argsort 函数对输入数组沿给定轴执行排序，返回排序后原数组的索引

numpy.argmax 返回指定轴的最大值的索引

numpy.argmin 返回指定轴的最小值的索引

numpy.nonzero 函数返回输入数组中非零元素的索引

numpy.where 返回输入数组中满足给定条件的元素的索引

numpy.extract 函数返回任何满足条件的元素


test11.py

numpy.dot 两个数组的点积

numpy.vdot 两个向量的点积

bumpy.inner 两个数组的内积

numpy.matmul 两个数组的矩阵积

numpy.linalg.det 计算输入矩阵的行列式

numpy.linalg.solve 求解线性矩阵方程

numpy.linalg.inv 寻找矩阵的乘法逆矩阵



