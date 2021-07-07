from collections import Iterable
from collections import Iterator

boo=isinstance([],Iterable)  #看列表是否是可迭代对象
boo1=isinstance((),Iterable)#看元组是否是可迭代对象
boo2=isinstance({},Iterable)#看字典是否是可迭代对象
boo3=isinstance("string",Iterable)#看字符串是否是可迭代对象

bo=isinstance([],Iterator)#看列表是否是可迭代器
bo1=isinstance((),Iterator)#看元组是否是可迭代器
bo2=isinstance({},Iterator)#看字典是否是可迭代器
bo3=isinstance("string",Iterator)#看字符串是否是可迭代器


b=isinstance(iter([]),Iterator)
b1=isinstance(iter(()),Iterator)
b2=isinstance(iter({}),Iterator)
b3=isinstance(iter("string"),Iterator)

print(boo,boo1,boo2,boo3) #True True True True
print(bo,bo1,bo2,bo3) #False False False False
print(b,b1,b2,b3)  #True True True True


#验证列表
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")  #1 2 3 4
print("\n")
    
#也可以使用 next() 函数：
import sys         # 引入 sys 模块
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()

#同等也可以验证元组和字典和字符串的使用
#我就不一一演示了
