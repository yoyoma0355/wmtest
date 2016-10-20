#! /usr/bin/env python
# -*- coding: utf-8 -*-



'''
目标：学会python中sys.argv的用法。
1)命令行办输入： cd /d E:\3--rms_test_api\1--summery_detail\wmtest
                 dir
                 python test_5_20161020.py --version    #输出固定版本号
                 python test_5_20161020.py --help    #输出固定文字
                 python test_5_20161020.py test_5_20161020.py   #输出该文件的所有内容。一行一行输出
'''
import sys

def readfile(filename):  #从文件中读出文件内容
    '''Print a file to the standard output.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line, # notice comma  分别输出每行内容
    f.close()

if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()
else:
    print sys.argv
    print len(sys.argv)
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

