#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#20190326

#test5
#古灵阁金币兑换
#待解决：当input函数获取的内容为字符型时，会报错。当更换为数字即不会出问题。
print('古灵阁金币兑换')
help=input('您好，欢迎光临古灵阁，请问您需要帮助吗？需要=1 or不需要=2？')
print(help)

if help==1:
    choice=int(input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))
    
    if choice ==1:
        print('请去存取款窗口。')
        
    elif choice==2:
        print('金加隆和人民币的兑换率为1:51.3，既1金加隆=51.3人民币')
        money=input('请问您需要兑换多少金加隆呢？')
        print('好的，我知道了，您需要兑换'+str(money)+'金加隆。')
        print('那么，您需要付给我'+str(int(money)*51.3)+'人民币。')


    else:
        print('请去咨询窗口。')


else:
    print('好的，再见。')


#test6
#列表生成器
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

