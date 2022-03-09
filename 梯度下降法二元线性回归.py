# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:46:58 2022

@author: lenovo
"""
import matplotlib.pyplot as plt
import numpy as np
m=22
x0=np.ones((m,1))#m行一列矩阵元素全为1的矩阵
x1=np.arange(1,m+1).reshape(m,1)#arange生成列表指定开始1到结束m,把列表塑形成m行1列的矩阵
x=np.hstack((x0,x1))#矩阵水平块加块堆叠形成新矩阵

y = np.array([6,5,
    3, 4, 5, 5, 2, 4, 7, 8, 11, 8, 12,
    11, 13, 13, 16, 17, 18, 17, 19, 21
]).reshape(m, 1)#一维数组横着的塑形为竖着的
eta=0.01

def cost_function(theta,x,y):
    diff=np.dot(x,theta)-y#两矩阵相乘
    return (1/(2*m))*np.dot(diff.transpose(),diff)
def gradient_function(theta,x,y):
    diff=np.dot(x,theta)-y
    return (1/m)*np.dot(x.transpose(),diff)
def gradient_descent(x,y,eta):
    theta=np.array([1,1]).reshape(2,1)#两个theta两行一列
    gradient=gradient_function(theta,x,y)
    while not all(abs(gradient)<=1e-5):
        theta=theta-eta*gradient
        gradient=gradient_function(theta,x,y)
    return theta
# 根据数据画出对应的图像
def draw(x,y,theta):
    ax = plt.subplot(111)  #就是一个图里可以画多个子图,几行几列的,第几个)
    ax.scatter(x, y, s=30, c="red", marker="o")
    plt.xlabel("X")#设置x轴,y轴标签
    plt.ylabel("Y")
    y = theta[0] + theta[1]*x
    ax.plot(x, y)
    plt.show()

a=gradient_descent(x,y,eta)
b=cost_function(a,x,y)
print('final theta:',a)
print('cost_functionresult:',b)
draw(x1,y,a)



