#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#20190327

#test1
#记录生肖，根据年份来判断生肖
#chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

#year = int(input('请用户输入出生年份'))

#if(chinese_zodiac[year % 12]) == '狗':
 #   print('狗年运势')

#test2
#遍历序列
#for cz in chinese_zodiac:
 #   print(cz)

#test3
#遍历数字
#for i in range(1,13):
  #  print(i)

#test4
#遍历数字+字符串
#for year in range(2000,2019):
 #   print('%s 年的生肖是 %s' %(year,chinese_zodiac[year %12]))

#test5
def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#test6
from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point #这一行报错。。。
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))

#test7
def is_odd(n):
    return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
