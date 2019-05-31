# -*- coding:UTF-8 -*-
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np
import random

"""
函数说明:加载数据
Parameters:
	无
Returns:
	dataMat - 数据列表
	labelMat - 标签列表
"""
def loadDataSet():
	dataMat = []														#创建数据列表
	labelMat = []														#创建标签列表
	fr = open('testSet.txt')											#打开文件
for line in fr.readlines():											#逐行读取
		lineArr = line.strip().split()									#去回车，放入列表
		dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])		#添加数据
		labelMat.append(int(lineArr[2]))								#添加标签
	fr.close()															#关闭文件
return dataMat, labelMat    #返回

# """
# 函数说明:sigmoid函数
# Parameters:
# 	inX - 数据
# Returns:
# 	sigmoid函数
# """

def sigmoid(inX):
return 1.0 / (1 + np.exp(-inX))

# """
# 函数说明:梯度上升算法
# Parameters:
# 	dataMatIn - 数据集
# 	classLabels - 数据标签
# Returns:
# 	weights.getA() - 求得的权重数组(最优参数)
# 	weights_array - 每次更新的回归系数
# """

def gradAscent(dataMatIn, classLabels):
	dataMatrix = np.mat(dataMatIn)										#转换成numpy的mat
	labelMat = np.mat(classLabels).transpose()							#转换成numpy的mat,并进行转置
	m, n = np.shape(dataMatrix)											#返回dataMatrix的大小。m为行数,n为列数。
	alpha = 0.01														#移动步长,也就是学习速率,控制更新的幅度。
	maxCycles = 500														#最大迭代次数
	weights = np.ones((n,1))
	weights_array = np.array([])
for k in range(maxCycles):
		h = sigmoid(dataMatrix * weights)								#梯度上升矢量化公式
		error = labelMat - h
		weights = weights + alpha * dataMatrix.transpose() * error
		weights_array = np.append(weights_array,weights)
	weights_array = weights_array.reshape(maxCycles,n)
return weights.getA(),weights_array									#将矩阵转换为数组，并返回

# """
# 函数说明:改进的随机梯度上升算法
# Parameters:
# 	dataMatrix - 数据数组
# 	classLabels - 数据标签
# 	numIter - 迭代次数
# Returns:
# 	weights - 求得的回归系数数组(最优参数)
# 	weights_array - 每次更新的回归系数
# """

def stocGradAscent1(dataMatrix, classLabels, numIter=150):
	m,n = np.shape(dataMatrix)												#返回dataMatrix的大小。m为行数,n为列数。
	weights = np.ones(n)   													#参数初始化
	weights_array = np.array([])											#存储每次更新的回归系数
for j in range(numIter):
		dataIndex = list(range(m))
for i in range(m):
			alpha = 4/(1.0+j+i)+0.01   	 									#降低alpha的大小，每次减小1/(j+i)。
			randIndex = int(random.uniform(0,len(dataIndex)))				#随机选取样本
			h = sigmoid(sum(dataMatrix[randIndex]*weights))					#选择随机选取的一个样本，计算h
			error = classLabels[randIndex] - h 								#计算误差
			weights = weights + alpha * error * dataMatrix[randIndex]   	#更新回归系数
			weights_array = np.append(weights_array,weights,axis=0) 		#添加回归系数到数组中
del(dataIndex[randIndex]) 										#删除已经使用的样本
	weights_array = weights_array.reshape(numIter*m,n) 						#改变维度
return weights,weights_array