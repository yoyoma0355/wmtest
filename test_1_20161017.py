#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
变量x、y的值互换
题：在不借助第三个变量的情况下，把两个int的变量X、Y的值互换，用任何自己熟悉的编程语言完成
参考答案：思路如下X=X+Y; Y=X-Y; X=X-Y;  具体编程语言完成情况由面试官检查。
考察点：基本算法、语言基础。

'''

if __name__=='__main__':
    x=8
    y=9

    x=x+y
    y=x-y
    x=x-y
    print x,y
