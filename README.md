# Data_analysis

### 字符串

[字符串与字符数据（上）](https://mp.weixin.qq.com/s?src=11&timestamp=1532656122&ver=1023&signature=5eSYmrZlKAAG3dCOLSNtngg87KtuwrKztGegdpjCnVUiFCon5uM35F8X1g1VtBsTptpcrgHovIRpA0vl91BfsPhIyaVBhAWcmzhmtmjR*4-Oj7iF*DUjts1CXGCYE8m6&new=1)

[字符串与字符数据（下）](https://mp.weixin.qq.com/s?src=11&timestamp=1532656122&ver=1023&signature=5eSYmrZlKAAG3dCOLSNtngg87KtuwrKztGegdpjCnVWEvKvXoOaqgEd*4AoA1dnsOCD2hWV2tGNuBht9RPL4w83wMa-O1g2gyMPjVaxtdlw9xlgpY*EUfipgQJ4v-dML&new=1)

### 正则表达式

![](https://mmbiz.qpic.cn/mmbiz_png/6e7JRZQW8LPrMiaKGTGcc3eUkib9Q2kRMJkcp9Ljiaia0oTT40SfwwIMZIoBljveqFA2DicfYTAKCbfVhtn3FtAWSCQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)


(1) compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。  
语法格式为：  
```
re.compile(pattern[, flags])

pattern : 一个字符串形式的正则表达式
flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和' # '后面的注释
```
(2) re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。   
函数语法：  
```
re.match(pattern, string, flags=0)
```
(3) re.search 扫描整个字符串并返回第一个成功的匹配   
函数语法：   
```
re.search(pattern, string, flags=0)

re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
```
(4) findall   
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。    
语法格式为：   
```
findall(string[, pos[, endpos]])

string 待匹配的字符串。
pos 可选参数，指定字符串的起始位置，默认为 0。
endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
```

从字符串提取数字:  
```
def findnum(string):
    comp=re.compile('\d+')
    list_str=comp.findall(string)
    list_num=[]
    for item in list_str:
        item=int(item)
        list_num.append(item)
    return list_num
```
