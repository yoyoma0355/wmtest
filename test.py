#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
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







