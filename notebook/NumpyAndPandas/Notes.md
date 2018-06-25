### set集合

* 必须是set集合

```
 s.issubset(t) #判断s是否是t的子集  
 s.issuperset(t) #判断s是否是t的超集  
 s.union(t)    #返回s和t的并集  
 s.intersection(t)  #返回s和t的交集  
 s.difference(t)    #返回s与t的差集  
 s.symmetric_difference(t)    #返回异或集  
 s.copy()    #返回s的一个浅拷贝  
```
------------------------------------------------------------------------

### Map和Filter函数

map()函数接收一个列表和一个函数，它对列表里的每个元素调用一个函数进行处理，再将结果放进一个心列表里。  
下面这个例子，map()函数遍历seq中没饿过元素，把它乘以2，再把结果放入一个新列表，最后返回这个列表：  
```
seq = [1,2,3,4,5]  
result=list(map(lambda var:var*2,seq))  
#output: [2,4,6,8,10]
```

filter()函数略有不同，它接收一个列表和一个规则函数，在对列表里的每个元素调用这个规则函数之后，它把所有返回值为假的元素从列表中剔除，返回过滤后的子列表。  
```
seq=[1,2,3,4,5]  
result=list(filter(lambda x:x>2,seq))  
#output:[3,4,5]
```

-----------------------------------------------------------------------------

### Arange 和Linspace函数生成数组

arange()函数按照指定的步长返回一个等差数列。初开始和结束值之外，还可以自定义步长和数据类型。  
```
np.arange(3,7,2)  
#output:arange([3,5])  
```

linspace()返回的是将给定区间进行若干等分以后的等分点组成的数列。传入的参数包括开始值、结束值和具体多少等分。linspace()将这个区间等分后，把开始值、
结束值和每个等分点都放进一个numpy数组里。  

```
np.linspace(2.0,3.0,num=5)  
#output:array([2.0,2.25,2.5,2.75,3.0])
```

### 数据透视表（Pivot Tables）

<img class=""  data-src="https://mmbiz.qpic.cn/mmbiz_png/ldSjzkNDxll0yx0LAoz4Wib0As3P9gs1lQW0zvChlNDdTPuicgvS1K7Rtyibx6ic7w4DMRJPRrfPIiaMd5yUWlv9orw/640?wx_fmt=png" data-type="png" data-w="463" height="662.25pt" style="width: 80% !important; height: auto !important; visibility: visible !important;" width="347.25pt" _width="80%" src="https://mmbiz.qpic.cn/mmbiz_png/ldSjzkNDxll0yx0LAoz4Wib0As3P9gs1lQW0zvChlNDdTPuicgvS1K7Rtyibx6ic7w4DMRJPRrfPIiaMd5yUWlv9orw/640?wx_fmt=png&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1" data-fail="0">


### 多维列表合并  
list3=np.concatenate((list1,list2),axis=1)    #按列合并
