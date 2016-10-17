#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
读取二进制文件写入指定文件中
请编写以下功能的函数：读取指定二进制文件（a）并将文件内容写入另外一个指定的新文件（b），要求在在新文件的起始位置用一个整数（int）表示文件（a）的长度。
该题目的审查要点是：
	函数接口的设计是否正确、合理；
	函数开始是否检查参数的有效性；#会变的东西做为参数。
	文件操作：打开文件的参数、返回值的检查、是否在返回前关闭文件、文件读取方式；
	内存操作：是否释放了函数内部申请的内存；
	写入长度字段时的长度，是4字节还是sizeof(int)。
'''
import json
def read_text(file):
    txt_list = file.split('.')
    if txt_list[-1] != 'txt':
        return False
    f = open(file,'r')
    s = f.read()
    len_s= len(s)
    f.close()   #关闭文件
    return len_s
    print "2m"   #因为放在retrun后面所以就不执行了。


def write_text(file,len1):
    #增加对文件地址和长度的有效性验证
    txt_list = file.split('.')
    if txt_list[-1] != 'txt':
        return False
    f1 = open(file,'w')
    f1.writelines(str(len1))
    f1.close()  #关闭文件
    print "1m"   #如果是txt文件，则会打印，因为这里没有返回值。

if __name__=='__main__':
    file_a = r"E:\3--rms_test_api\data\test_a.txt"
    file_b = r"E:\3--rms_test_api\data\test_b.txt"
    read_f =read_text(file_a)
    print read_f
    wirte_f = write_text(file_b,read_f)
    print wirte_f
