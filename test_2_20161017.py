#! /usr/bin/env python
# -*- coding: utf-8 -*-

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

import re
def get_str_match(str1,str2):
    str_temp = list(enumerate(str1))
    for i in str_temp:
        if i[1]== str2[0].lower() or i[1]==str2[0].upper():
            s=i[0]
    return s
if __name__=='__main__':
    str1 = 'abcdefg'
    str2 = "abcdef"
    res_s = get_str_match(str1,str2)
    print res_s

