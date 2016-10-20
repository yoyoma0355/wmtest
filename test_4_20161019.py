#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
题目28	(本题无答案)：1-9全排列
写一个程序，输出1-9的所有全排列。

本文实例讲述了常规方法实现python数组的全排列操作。分享给大家供大家参考。具体分析如下：

全排列解释：从n个不同元素中任取m（m≤n）个元素，按照一定的顺序排列起来，叫做从n个不同元素中取出m个元素的一个排列。当m=n时所有的排列情况叫全排列。
这个还需要再理解。
'''

import sys

def perm(l):
  if(len(l)<=1):
    return [l]
  r=[]
  for i in range(len(l)):
    s=l[:i]+l[i+1:]
    p=perm(s)    #递归调用，两个return完了都到这里，递归的出口是什么我还没有理清楚。
    for x in p:
      r.append(l[i:i+1]+x)
  return r


if __name__=='__main__':
  """ default param is list(1,2,3,4,5) """
  l=[];
  if(len(sys.argv)<=1):
    """input=['%d' %(i) for i in xrange(1,6)]"""
    l=list((1,2,3,4,5,6,7,8,9))
  else:#input param looks like "2,3,4,5,6",no legal checks here.
    input=str(sys.argv[1])    #接收命令行参数
    l=input.split(",")
    for i in xrange(len(l)):
      l[i] = int(l[i])
  res=perm(l)
  print len(res)  #g1-9的全排列的个数为362880种
  #print perm(l)

