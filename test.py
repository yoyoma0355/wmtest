#! /usr/bin/env python
# -*- coding: utf-8 -*-


'''
题目28	(本题无答案)：1-9全排列
写一个程序，输出1-9的所有全排列。

本文实例讲述了常规方法实现python数组的全排列操作。分享给大家供大家参考。具体分析如下：

全排列解释：从n个不同元素中任取m（m≤n）个元素，按照一定的顺序排列起来，叫做从n个不同元素中取出m个元素的一个排列。当m=n时所有的排列情况叫全排列。


def perm(l):
  if(len(l)<=1):
    return [l]
  r=[]
  for i in range(len(l)):
    s=l[:i]+l[i+1:]
    p=perm(s)
    for x in p:
      r.append(l[i:i+1]+x)
  return r

调用方法：
if __name__=='__main__':
  """ default param is list(1,2,3,4,5) """
  l=[];
  if(len(sys.argv)<=1):
    """input=['%d' %(i) for i in xrange(1,6)]"""
    l=list((1,2,3,4,5))
  else:#input param looks like "2,3,4,5,6",no legal checks here.
    input=str(sys.argv[1])
    l=input.split(",")
    for i in xrange(len(l)):
      l[i] = int(l[i])
  print perm(l)

希望本文所述对大家的Python程序设计有所帮助。

'''




if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':  #当命令行参数为-- version，显示版本号
        print 'Version 1.2'
    elif option == 'help':  #当命令行参数为--help时，显示相关帮助内容
        print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
  --version : Prints the version number
  --help    : Display this help'''
    else:
        print 'Unknown option.'
    sys.exit()
else:
    for filename in sys.argv[1:]: #当参数为文件名时，传入readfile，读出其内容
        readfile(filename)

