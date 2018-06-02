
## 描述

### 贷款数据分析

该文件包含完整的贷款数据，所有贷款通过所规定的时间段，包括当前贷款状况（当前，晚，全额支付等）和最新的付款信息。
包含“当前”的贷款数据的文件包含完整的贷款数据，用于通过以前完成的日历季度发行的所有贷款。[**点击**](https://www.lendingclub.com/info/download-data.action)
以下载文件的完整版本。本例使用的数据集是2016Q1数据集。

> * **seaborn绘图**

> * **select_dtypes** 将数据类型进行分类， 再用 **describe** 方法返回的统计值

> * **drop()** 删除空值

> * **quantile()** 实现分位数

> * **.loc[:,data.columns.str.contains(strings)],** 取列名中包含strings字母的所有变量

> * **groupby().agg()** 组合分组统计

> * **scipy.stats.norm** 在seaborn中原图的基础上绘制连续正太分布的折线

> * **Dataframe.ploy.pie()** 直接用dataframe绘制饼图

> * **drop()** 删除空值

> * **drop()** 删除空值

> * 根据两个列聚合联合多个列生成表
