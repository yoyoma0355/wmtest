#! /usr/bin/env python
# -*- coding: utf-8 -*-


func1()   #这个会失败的原因是，func1的def代码还未执行

def func1():
    print(func2())

func2()   #这里失败原因同上，所在def在前，调用在后。
def func2():
    return "hello"

func1()
func2()


class rec:
    pass

rec.name='wangmin'
rec.age='34'
rec.sex='woman'
rec.job='it'

print rec.age
'''
#
#pickup_day =(1,2)
#
#def get_max_pickup_day(self):
#    for x in self.pickup_day:
#        re= self.get_api(0)
#        if re==():
#            return x
#            break
#        continue
#    return x


#
#
#
#
#file = open(r'E:\3--rms_test_api\data\20160927141851162_1_mstbillrev.json','r')
#for (num,value) in enumerate(file):
#    print "line:",num,"is:",value
#file.close()

'''
实现字符串匹配功能
请编写以下功能的函数：在一个字符串（str1）中查找另外一个串（str2）的最大前缀，比如str1 = "abcdefg", str2 = "descript"，
那么最大前缀是"de"，返回这个前缀在str1中的位置。要求函数是对大小写不敏感的。该题目的审查要点是：
	循环使用是否正确
	是否有必要的效率考虑，比如一些同学会在循环里面调用strlen(str1)；
	是否满足了大小写不敏感的要求
	是否有不必要的内存申请和串拷贝
	写一个strcmp程序，功能和C库相同

'''
#
#import re
#def get_str_match(str1,str2):
#    str_temp = list(enumerate(str1))
#    for i in str_temp:
#        if i[1]== str2[0].lower() or i[1]==str2[0].upper():
#            s=i[0]
#    return s
#if __name__=='__main__':
#    str1 = 'abcdefg'
#    str2 = "abcdef"
#    res_s = get_str_match(str1,str2)
#    print res_s


'''
变量x、y的值互换
题：在不借助第三个变量的情况下，把两个int的变量X、Y的值互换，用任何自己熟悉的编程语言完成
参考答案：思路如下X=X+Y; Y=X-Y; X=X-Y;  具体编程语言完成情况由面试官检查。
考察点：基本算法、语言基础。

'''

#if __name__=='__main__':
#    x=8
#    y=9
#
#    x=x+y
#    y=x-y
#    x=x-y
#    print x,y

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


