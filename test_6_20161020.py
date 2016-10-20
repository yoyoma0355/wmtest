#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
目标：练习带条件的for循环   for中带for的语句
题目：1)100以内所有偶数
     2) 100以内所有数的乘方倒排序
'''

def even(number):
    n= number
    for j in (i for i in range(1,n) if i%2==0):
        print j


def stort1(number):
    n=number
    l=sorted((x**2 for x in range(1,n)),reverse=True)
    print l

if __name__ =="__main__":
    even(100)
    stort1(100)