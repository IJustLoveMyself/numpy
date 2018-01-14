#************coding:utf-8****************
import numpy as np

# numpy数据类型
# 1.	bool_存储为一个字节的布尔值(真或假)
# 2.	int_默认整数，相当于 C 的long，通常为int32或int64
# 3.	intc相当于 C 的int，通常为int32或int64
# 4.	intp用于索引的整数，相当于 C 的size_t，通常为int32或int64
# 5.	int8字节(-128 ~ 127)
# 6.	int1616 位整数(-32768 ~ 32767)
# 7.	int3232 位整数(-2147483648 ~ 2147483647)
# 8.	int6464 位整数(-9223372036854775808 ~ 9223372036854775807)
# 9.	uint88 位无符号整数(0 ~ 255)
# 10.	uint1616 位无符号整数(0 ~ 65535)
# 11.	uint3232 位无符号整数(0 ~ 4294967295)
# 12.	uint6464 位无符号整数(0 ~ 18446744073709551615)
# 13.	float_float64的简写
# 14.	float16半精度浮点：符号位，5 位指数，10 位尾数
# 15.	float32单精度浮点：符号位，8 位指数，23 位尾数
# 16.	float64双精度浮点：符号位，11 位指数，52 位尾数
# 17.	complex_complex128的简写
# 18.	complex64复数，由两个 32 位浮点表示(实部和虚部)
# 19.	complex128复数，由两个 64 位浮点表示(实部和虚部)
#
# numpy.dtype(object, align, copy)可以用来自定义数据类型
# Object：被转换为数据类型的对象。
# Align：如果为true，则向字段添加间隔，使其类似 C 的结构体。
# Copy：生成dtype对象的新副本，如果为flase，结果是内建数据类型对象的引用。

student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')])
a = np.array([('abc',21,50),('xyz',18,75)], dtype = student)
print a['name'] # ['abc' 'xyz']
print a['age'] # [21 18]
print a['marks'] # [ 50.  75.]

# 'b'：布尔值
# 'i'：符号整数
# 'u'：无符号整数
# 'f'：浮点
# 'c'：复数浮点
# 'm'：时间间隔
# 'M'：日期时间
# 'O'：Python 对象
# 'S', 'a'：字节串
# 'U'：Unicode
# 'V'：原始数据(void)
# 字母后面跟得数字是长度