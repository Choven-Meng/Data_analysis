### 两个列表的交并补（numpy）

<img src="https://images2015.cnblogs.com/blog/981211/201610/981211-20161002143706024-92494456.png" >

----------------------
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

-----------------------

### 获得索引位置

```
np.nonzero(data[col]==da) #获得索引位置，返回col列值为da的所有位置组成的np数组
# output:    (array([0, 2, 4], dtype=int64),)
```

```
# 返回最小值索引位置
np.argmin(a,axis = None/0/1)
```


-----------------------------------

### 按条件转换值，清洗重新赋予值

```
#将class列的versicolor转换成Iris-versicolor
iris_data.loc[iris_data['class'] == 'versicolor', 'class'] = 'Iris-versicolor'
iris_data.loc[iris_data['class'] == 'Iris-setossa', 'class'] = 'Iris-setosa'
```

```
#利用字典转换
os_type_mapping = {'h5':'H5','android':'Android','ios':'IOS'}
f = lambda x : os_type_mapping.get(x,x)
userInfor31_32.os_type = userInfor31_32.os_type.map(f)
```

```
# 利用transform转换
@data
   a  b  c  d  e
li    1  2  3  4  5
chen  2  1  1  2  2
wang  1  2  3  4  5
zhao  2  1  1  2  2
qian  1  2  3  4  5

# data里每个元素位置的取值由transform函数的参数函数计算
data.group(['ss','kk','kk','ss','ss']).ransform(np.mean) # data里每个位置元素取对应分组列的均值

```

```
# re 模块
 pattern = re.compile(r'</?\w+[^>]*>', re.S)  # 匹配特殊字符
 comment = re.sub(pattern, '', comment)   # 将匹配的特殊字符转化为空值
```

### 筛选

```
iris_data = iris_data.loc[(iris_data['class'] != 'Iris-setosa') | (iris_data['sepal_width_cm'] >= 2.5)]

iris_data.loc[(iris_data['class'] == 'Iris-versicolor') & (iris_data['sepal_length_cm'] < 1.0)]
```

```
 #逻辑运算
 # 筛选出df列表中comments列种小于等于10000大于等于1000的值
df[(df.comments>=1000) & (df.comments<=10000)]
```

#### 字符串匹配

```
#字符匹配
# df列表中title列中的值包含‘台电’的数据
df[df.title.str.contains('台电', na=False)]
```
------------------

### 将一维转换为二维

```
>>> a = np.array((1,2,3))
>>> b = np.array((2,3,4))
>>> np.column_stack((a,b))
array([[1, 2],
       [2, 3],
       [3, 4]])
```

---------------

### 窗函数

窗函数（window function）经常用在频域信号分析中  
```
df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
df.rolling(2).sum()
#output:    B    NaN     1.0      3.0        NaN           NaN
```

-------------------

### 时间模块datetime

```
# 将时间格式转化为日期格式（保留日期去掉时间）
data['交易时间'] = pd.to_datetime(data['交易时间']).dt.normalize()
```
```
# 将字符串转换为时间格式
datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")

# 今天的日期
today = datetime.date.today()

# 上月的日期
from  dateutil.relativedelta import relativedelta
T_M = datetime.date.today() - relativedelta(months=+1)

# 昨天的日期(T)
T = (today + datetime.timedelta(days=-1)).strftime('%Y-%m-%d') # 得到的是字符串
T = datetime.datetime.strptime(T, "%Y-%m-%d")
T = T.date() # 获得日期格式的日期
```
