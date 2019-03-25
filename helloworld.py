#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#我的第一个Python程序-20190325

print("***************************************************")
# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
print("利用递归函数计算阶乘")
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))

# 利用递归函数移动汉诺塔:
print("利用递归函数移动汉诺塔")
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')


print("***************************************************")
def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
age = int(input('Input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    
# 计算1+2+3+...+100:
print("***************************************************")
print("计算1+2+3+……+100")
sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)

# 计算1x2x3x...x100:
print("***************************************************")
print("计算1x2x3x...x100")
acc = 1
n = 1
while n <= 100:
    acc = acc * n
    n = n + 1
print(acc)

# hello world
print("***************************************************")
print "hello world!"


#字典
print("***************************************************")
print("字典示例")
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))


print("***************************************************")
x = abs(100)
y = abs(-20)
print(x, y)
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))




