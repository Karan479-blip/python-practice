
Data manipulation is a fundamental skill in data science and analysis, enabling data scientists to transform, clean, and reshape data for further exploration and modeling.
import pandas as pd
     

data=[10,20,30,40]
s=pd.Series(data,index=["a","b","c","d"])
     

print("Series from list:")
print(s)
     
Series from list:
a    10
b    20
c    30
d    40
dtype: int64

import numpy as np
     

array_data=np.array([1.1,2.2,3.3,4.4])
s_from_array=pd.Series(array_data,index=["x","y","z","w"])
     

print("Series from array:")
print(s_from_array)
     
Series from array:
x    1.1
y    2.2
z    3.3
w    4.4
dtype: float64

dict_data={"Apple":100,"Banana":200,"Cherry":300}
s_from_dict=pd.Series(dict_data)
     

print("Series from dictionary:")
print(s_from_dict)
     
Series from dictionary:
Apple     100
Banana    200
Cherry    300
dtype: int64

print("Index:",s.index)
print("Values:",s.values)
print("Data type:",s.dtype)
print("Size:",s.size)
     
Index: Index(['a', 'b', 'c', 'd'], dtype='object')
Values: [10 20 30 40]
Data type: int64
Size: 4

print("First two elements:",s.head(2))
print("Last two elements:",s.tail(2))
print("Sorted values:",s.sort_values())
print("Mean of the Series:",s.mean())
     
First two elements: a    10
b    20
dtype: int64
Last two elements: c    30
d    40
dtype: int64
Sorted values: a    10
b    20
c    30
d    40
dtype: int64
Mean of the Series: 25.0
