## 字符串

* 字符串长度

```
select length('中国');  
output：2
```

* 替换字符串
  * overlay (string placing string from int [for int])
  * replace (string text, from text, to text)
  * translate (string text, from text, to text)

``` 
-- 其中第一个int是开始位置，第二个int是长度，如果没有第二个int则长度默认为第二个字符串的长度
select overlay('Txxxxas' placing 'hom' from 2 for 4);  
output：Thomas
```

```  
-- 将第一个字符串中的第二个字符串替换成第三个字符串    
select replace('Txxxxas','xxxx','hom');    
output：Thomas
```

```
-- 把string中from字符替换成对应to中的字符，如('text','tx','nd')中t->n,x->d,替换后结果为nedn;  -- 如果from比to长，则删除from多出的字符;  如果from中有重复字符，对应顺序也是一一对应的，
-- 但是重复字符以第一个为准，如('txxxa','xxx','abcd'),结果为taaad  

select translate('Txxxxas','xxxxa','hom');  
output:Thhhhs

select translate('Txxxxas','Txas','hom');  
output:hoooom

select translate('txxxa','xxxa','abcd');  
output:taaad
```

* 字符串位置   
  * position (substring in string)
  * strpos (string, substring)

```
select position('lo' in 'hello');  
output：4

select strpos('hello','llo');  
output：3
```

* 截取字符串  
  * substring (string [from int] [for int])

```
select substring('hello world' from 2 for  4);  
output：ello

select substring('hello world',2,3);  
output：ell
```

* 正则表达式匹配  

```
select substring('hell world' from '...$');  
output：rld

select substring('Thomas' from '%#"o_a#"_' for '#');  
output：oma
```

* 删除字符串两边的空白或字符    
  * trim ([both] characters from string)

```
select trim(both 'x' from 'xxjdhdxxxx');  
	
select btrim('xxjdhdxxxx','x');  
	
output：jdhd
```

* 分割字符串  
  * split_part(string text, delimiter text, field int)

```
-- 将字符串string以delimiter进行分割，并返回第field个子串 
select split_part('shus#sssd#3','#',2);  
output：sssd
```

* 字符串连接

  * string || string

```
SELECT substr('2019-07-06 00:00:00',1,7)||'-01';
output: 2019-07-01
```

## 时间

* 字符串与时间格式相互转换

  * to_timestamp(text, text)
  * to_timestamp(text, text)

  * timestamp text
  * to_char(timestamp, text)

```
-- 字符串转换成时间戳格式
SELECT to_timestamp('2019-07-06','yyyy-MM-dd') as TIMESTAMP;
```

```
-- 字符串转换成时间格式
SELECT to_date('2019-07-06','yyyy-MM-dd') as date;
```

```
-- 时间转字符串
SELECT to_char(CURRENT_DATE, 'YYYY-MM-DD')
```

* 时间加减
  * interval

```
-- 年、月、日、周、时、分、秒
select CURRENT_DATE + interval '2 year 1 month';
output:2021-08-17 00:00:00
```

```
-- 月末
SELECT date_trunc('month', CURRENT_DATE) + interval '1 month -1 day'
output:2019-07-31 00:00:00+08
```

* 时间截取
  * date_part(text, timestamp)
  *  extract(field from timestamp)
  * date_trunc(text, timestamp) 

```
-- 输出当前时间时数
SELECT date_part('hour', now())
```

```
-- 输出当前月份
extract(month from now());
```

```
-- 截取到指定精度，year-当年第一天，month-当月第一天，day-当天零点，hour-当前时间零分
SELECT date_trunc('month', timestamp'2019-07-17 12:30:40')
output: 2019-07-01 00:00:00
```

* 时间间隔
   * age(timestamp, timestamp)

```
select age(TIMESTAMP'2018-08-31',TIMESTAMP'2019-09-01');
output:-1 years -1 days
```

```
-- 获取时间间隔的年份
select extract(YEAR from age(TIMESTAMP'2018-08-31',TIMESTAMP'2019-09-01'));
output:-1
```



