def decorator(cls):  #修饰函数
    class wrapper():
        def __init__(self, *args, **kwargs):
            print("内部类修饰1")
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self,name):  #实例的属性的调用都会对 __getattr__的调用
            print("trace:",name)
            return getattr(self.wrapped,name)
    return wrapper

@decorator  # 等价于cls = decorator(cls)
class cls():  #修饰类就等价于wrapper
    def __init__(self, x, y):
        self.attrx = x
        self.attry = y
    def method(self):
        return self.attrx, self.attry

c = cls(3, 4)   #c是Wrapper的实例
print(c.attrx)  #cls类的实例上的属性获取都会调用Wrapper类中的__getattr__逻辑,c是Wrapper的实例,这样有利于装饰器的实例创建调用重定向
print(c.attry)
print(c.method())
