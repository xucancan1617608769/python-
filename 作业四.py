import matplotlib.pylab as pl
import numpy as np

def huatu(fn):#修饰函数
    #定义一个嵌套函数
    def hua(*args,**kwargs):
        x1,y1=fn(*args,**kwargs)
        print(x1.shape,y1.shape)
        #s指大小，c指颜色，marker指符号形状
        pl.scatter(x1,y1,s=500,c=u'r',marker=u'.')
        pl.show()
    return hua
    

@huatu  #相当于randompoint=huatu(randompoint)
def randompoint(i):  #被修饰函数
    x=np.random.random(i)
    y=np.random.random(i)
    return x,y

randompoint(100)
