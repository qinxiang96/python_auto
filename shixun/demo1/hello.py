#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   hello.py
@Time    :   2025/01/05 13:06:09
@Author  :   qinxiang 
@Version :   1.0
@Site    :   https://github.com/qinxiang96
@Desc    :   None
'''

print("hello world")
a = 0
print("这个是变量：",a)
# 关键字
import keyword
print(keyword.kwlist)
# 格式化输出
print("这个是变量：%d" %a)
print("我的名字是%s,我的国籍是%s"%("qinxiang","China"))
# 列表
list = ["小张","小王","小李"]
print(list[0])
for name in list:
    print(name)
# find_name = input("输入查找的姓名：\n")
# if find_name in list:
#     print("找到了")
# else:
#     print("没有找到")
# 元组
tup1 = ("a","b","c")
print(tup1[0])
# 字典
info = {"name":"qinxiang","age":18}
print(info["name"])
info["id"] = 8
print(info["id"])
# 定义函数
def printInfo():
    print("人生苦短，我用Python")
printInfo()

# 文件操作
f= open("test.txt","w")
f.write("hello")
f.close()#关闭后，其他程序才能访问该文件

# 异常处理
try:
    f= open("test1.txt","r")
except Exception as e:
    pass
    print(e)
finally:
    f.close()
