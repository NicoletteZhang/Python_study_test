#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#20190326


#test1打印皮卡丘
print('''
　　 へ　　　　　／|
　　/＼7　　　 ∠＿/
　 /　│　　 ／　／
　│　Z ＿,＜　／　 　 /`ヽ
　│　　　　　ヽ　 　 /　　〉
　 Y　　　　　`　  /　　/
　ｲ●　､　●　⊂⊃ 〈　　/
　()　 ^　　　|　＼〈
　　>ｰ ､_ ィ　│   ／／
　 / へ/ 　ﾉ＜|  ＼＼
　 ヽ_ﾉ　 (_ ／│ ／／
　　7　　　　 　　|／
　　＞―r￣￣`ｰ―__`
''')

#test2
#待解决：如何在一行中打印文字和变量值，有几种方法？
a = float(input('请输入你的体重(kg)：'))
b = float(input('请输入你的身高(m)：'))
bmi = a/(b*b)
print('你的bmi值是：'+str(bmi))
if bmi >= 28.0:
    print('肥胖')
elif bmi >= 24.0:
    print('过重')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')

#test3
#一人饮酒醉
number1 = 1
number2 = 2
unit1 = '人'
unit2 = '眼'
line1 = '我编程累'
line2 = '是bug相随'
sentence1 = '碎掉的节操满地堆'
sentence2 = '我只求今日能早归'

print(str(number1)+unit1+line1+sentence1)
print(str(number2)+unit2+line2+sentence2)

#test4
#非酋
#转换为字符串形式：需要使用str()函数将数据转换为字符串形式,eg:【str(int(float(number)))】
#数据拼接：使用数据拼接符号`+`，将字符串型变量拼接
slogan = '脸黑怪我咯'
number = '7.8'
unit = '张'
sentence = '蓝票一个SSR都没有'

print(slogan+str(int(float(number)))+sentence)


