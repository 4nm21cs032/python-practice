'''
    Pandas:
        - open source python libaray
        - used for data manipulation and analysis
        - Built on top of numpy
        - provides the powerful data strutures like dataframe and series for handling strutured data.
    Applications:
        -Data cleaning
        -Data anlysis
        -time series analysis
        -data integration and trasnformation
        -ML
        -Financial analysis

    NumPy vs Pandas

    - Numpy : Numerical computing
        > supoorts matrix and arrays
        > use lot of math fns to compute mt and arr
    - pandas : data manipulation and analysis
        > built on top of numpy
        > provide high level DS like Dataframe and Series
'''
import pandas as pd
# data={
#     'name':['alice','bob','charlie'],
#     'age':[25,24,21],
#     'score':[80,60,50]
# }
# df=pd.DataFrame(data)
# print(df)
'''
          name  age  score
    0    alice   25     80
    1      bob   24     60
    2  charlie   21     50
'''

# print(df.describe)

# data=[10,20,30,40]
# series=pd.Series(data,index=['a','b','c','d'])
# print(series)
'''
    a    10
    b    20
    c    30
    d    40
    dtype: int64
'''

# data={
#     'name':['alice','bob','charlie','swaroop','jack','john','jill'],
#     'age':[25,34,19,34,32,23,32],
#     'score':[80,60,50,55,66,77,88]
# }
data={
    'name':['alice','bob','charlie'],
    'age':[25,34,19],
    'score':[80,60,50]
}
df1=pd.DataFrame(data)
# print(df1)
# print(df1['name'])

# print(df1.head())   # default first 5 rows shown
'''
          name  age  score
    0    alice   25     80
    1      bob   34     60
    2  charlie   19     50
    3  swaroop   34     55
    4     jack   32     66
'''

# access columns
# print(df1['name'])
# First row
# print(df1.iloc[0])
'''
    name     alice
    age         25
    score       80
'''

# df2=pd.read_csv('data.csv')
# print(df2)

# Csv created
# df1.to_csv('output.csv',index=False)
# new column added
# df1['country']=['USA','Canada','UK','India','AUS','SA','WI']
df1['country']=['USA','Canada','UK']
# print(df1)

# filter rows
filt_df=df1[df1['age']>28]
# print(f'Filtered DataFrame:\n{filt_df}')
print('--------------------------------------')
sort_df=df1.sort_values('score',ascending=True)
# print(f'Sorted Data Frame:\n{sort_df}')

print('--------------------------------------')

import numpy as np
df1['Bonus']=np.random.randint(100,500,size=len(df1))
print(df1)

import matplotlib.pyplot as plt
df1['score'].plot(kind='bar')
# plt.show()

idx=pd.Index([1,2,3],name="customIndex")
series=pd.Series([10,20,30],index=idx)
print(series)


arrays=[['USA','USA','UK'],['Chicago','NewYork','london']]
index=pd.MultiIndex.from_arrays(arrays,names=('country','city'))

data=[10,20,30]
series=pd.Series(data,index=index)
print(series)