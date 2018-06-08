#question: For a given animal find frequency of all the attributes 
#DATA
#class_id  animal_id    attributes
#   1        21         walk, talk, sleep
#   1        22         eat, sleep
#   1        21         cry,laugh, sleep
#   1        21         dance, cook, walk

from collections import Counter
cluster_attribites=pd.DataFrame({'attribute_frequency' : data.groupby('animal_id').apply(
    lambda x: str(Counter([item for sublist in [i.split(',') for i in list(data['attributes'])] for item in sublist])))}).reset_index()
    
#output:    animal_id	       attribute_frequency
#         0	  21	            Counter({' sleep': 3, 'walk': 1, ' talk': 1, '...
#         1	  22	            Counter({' sleep': 3, 'walk': 1, ' talk': 1, '...

----------------------------------------------------------------------------------------

In []: df
Out[]: 
   a          b    c
0  1  [1, 2, 3]  foo
1  1     [2, 5]  bar
2  2     [5, 6]  baz

In []: df.groupby('a').agg({'b': 'sum', 'c': lambda x: ' '.join(x)})
Out[]: 
         c                b
a                          
1  foo bar  [1, 2, 3, 2, 5]
2      baz           [5, 6]

-----------------------------------------------------------------

useful_data.groupby('single_kv', as_index=False).agg(lambda x : str(Counter(x.cleaned_single_sv).most_common(50)))

#single_kv, cleaned_single_sv are columns
#If the above gives error like Series does not have the column cleaned_single_sv, then instead of using multiple columns in groupby, 
#first concat these columns create a single column out of them and then groupby 

-------------------------------------------------------------

#groupby with agg and size within agg dictionary [then use np.size instead of size()]
final_df.groupby('source').agg({'col_name':np.size, 'col2_name':np.sum}).reset_index()

-------------------------------------------------------------
#group by with sorting
df.groupby('team').apply(lambda x: ','.join(sorted(x.user)))
OR
df.groupby('team').agg({'user' : lambda x: ', '.join(x)})

-------------------------------------------------------------

#Dataframe a column include elements
df['A'].isin([1]) 
#return True or False for every index

df[df['A'].isin([3, 6])]

--------------------------------------------------------------

#Order by
data = data.sort_values(['a','b'])
#'a' is first key, 'b' is second key. sort ‘b’ on the basic of sort 'a'

---------------------------------------------------------------

#Count distinct  (groupby for difference column)
In [1]: table
Out[1]: 
           num     date
0           1     201301
1           1     201301
2           2     201301
3           1     201302
4           2     201302
5           2     201302
6           3     201302

In [2]: table.groupby('date').num.nunique()
Out[2]: 
date
201301       2
201302       3

------------------------------------------------------------------

# Count distint for same column
In [3]: table.date.value_counts()
Out[3]: 
201302    4
201301    3

#Different types entries mentioned in "activity" column as seperate columns. The entries of these cells will be number of occurrences
df.groupby('name')['activity'].value_counts().unstack().fillna(0)
---------------------------------------------------------------------

#Creating empty dataframe
df = pd.DataFrame({c: np.repeat(0, [nrow]) for c in data['PAGENO'].unique()})

#Assigning values to a cell of a dataframe
#Populating the dataframe
#list(row)[1]返回data的value构成的列表，list(list(row)[1])[1]返回列数据
for row in data.iterrows():
	if list(list(row)[1])[1] in data['PAGENO'].unique():
		df.set_value(index=di[list(list(row)[1])[0]], col=list(list(row)[1])[1], value=list(list(row)[1])[2])
        
 --------------------------------------------------------------------------

