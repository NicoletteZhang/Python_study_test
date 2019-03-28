#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#20190328_test2

#类与实例
#面向过程编程，自上而下，更适合机器执行
#user1 = {'name':'tom','hp':100}
#user2 = {'name':'jerry','hp':80}

#def print_role1(rolename):
#    print('name is %s , hp is %s' %(rolename['name'], rolename['hp']))

#print_role1(user1)


#面向对象编程，更符合人的认知习惯
class Player():   #定义一个类，把相同特性的东西进行归类;类的名字第一个字母大写

    def __init__(self, name, hp ,occu):    #特殊方法，第一个参数一定要带self
        #在变量前加两个下划线，变量就不能被访问到了
        self.__name = name    #变量被称作属性
        self.hp = hp
        self.occu = occu
        
    def print_role2(self):    #定义一个方法
        print('%s: %s %s' %(self.__name, self.hp, self.occu))

    #通过方法去修改变量值，而不直接修改。
    #在变量前加两个下划线
    def updateName(self, newname):   
        self.name = newname
        
class Monster():
    '定义怪物类'
    pass

user11 = Player('tom',100,'war')   #类的实例化
user22 = Player('jerry',80, 'master')
user11.print_role2()
user22.print_role2()

user11.updateName('wilson')
user11.print_role2()

user11.name = ('aaa')
user11.print_role2()
