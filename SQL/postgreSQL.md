## 操作字符串


`select  length('中国');
输出：2`

<!--替换字符串，其中第一个int是开始位置，第二个int是长度，如果没有第二个int则长度默认为第二个字符串的长度-->

`select overlay('Txxxxas' placing 'hom' from 2 for 4);
输出：Thomas`

<!--
替换字符串，将第一个字符串中的第二个字符串替换成第三个字符串
-->
`select replace('Txxxxas','xxxx','hom');
输出：Thomas`

<!--
把string中from字符替换成对应to中的字符，如('text','tx','nd')中t->n,x->d,替换后结果为nedn;如果from比to长，则删除from多出的字符;如果from中有重复字符，对应顺序也是一一对应的，但是重复字符以第一个为准，如('txxxa','xxx','abcd'),结果为taaad
-->

`select translate('Txxxxas','xxxxa','hom');`
`output:Thhhhs`
 
`select translate('Txxxxas','Txas','hom');`
`output:hoooom`

`select translate('txxxa','xxxa','abcd');`
`output: taaad`

<!--字符串位置-->

`select position('lo' in 'hello');`
`output：4`

`select strpos('hello','llo');`
`output：3`

<!--截取字符串-->

`select substring('hello world' from 2 for  4);`
`输出：ello`

`select substring('hello world',2,3);`
`输出：ell`

<!--正则表达式匹配-->
`select substring('hello world' from '...$');`
`output：rld`

`select substring('Thomas' from '%#"o_a#"_' for '#');`
`output：oma`

<!--删除字符串两边的空白或字符-->
`select trim(both 'x' from 'xxjdhdxxxx');`
`select btrim('xxjdhdxxxx','x');`
`output：jdhd`

<!--将字符串string以delimiter进行分割，并返回第field个子串-->
`select split_part('1#2#3','#',2);`
`output：2`



