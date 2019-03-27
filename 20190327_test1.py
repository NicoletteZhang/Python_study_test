#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#20190327

#test1
#记录生肖，根据年份来判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

year = int(input('请用户输入出生年份'))

if(chinese_zodiac[year % 12]) == '狗':
    print('狗年运势')

#test2
#遍历序列
for cz in chinese_zodiac:
    print(cz)

#test3
#遍历数字
for i in range(1,13):
    print(i)

#test4
#遍历数字+字符串
for year in range(2000,2019):
    print('%s 年的生肖是 %s' %(year,chinese_zodiac[year %12]))
