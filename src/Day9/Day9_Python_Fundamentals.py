#Pandas Series
import pandas as pd

c1=pd.Series([10,20,30])
c2=pd.Series([10,20,30], index=['a','b','c'])
print(c1)
print(c2)


#indexing and selection
marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])

#Boolean Masking
scores=pd.Series([45, 67, 89, 34, 90])
passed = scores[scores > 60]
print(passed)

#Missing Values
data = pd.Series([10, None, 30, None])
print(data.isnull())
print(data.fillna(0))
print(data.fillna(5))

#Vectorized String Operation
names = pd.Series(['Alice', 'bob', 'CHARLIE'])
print(names.str.lower())
print(names.str.contains('b'))
print(names.str.endswith('b'))
print(names.str.startswith('A'))