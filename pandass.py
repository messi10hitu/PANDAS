import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
*pandas is an open source data analysis written in python
*it lecerages the power and speed of numpy to make data analysis and processing easy for data scientist
*it provides rich and highly robust data operation
'''

# dict1 = {"name": ["python_all_concept", "rohan", "shubh"], "marks": [95, 78, 85],
#          "city": ["delhi", "mumbai", "bengalore"]}
# print(dict1)
# print(dict1.keys())
# df = pd.DataFrame(dict1)  # dataframe is an excel sheet which we can use in the python
# print(df)
#
# df.to_csv('friends.csv')  # csv = comma seperated values
# df.to_csv('friends_index_false.csv', index=False)  # create the csv file with no index
# df.index = ['first', 'second', 'third']
# print("-------")
# print(df)
#
# print(df.head(2))  # starting two values
# print(df.tail(2))  # last two values
# print(df.describe())  # it gives us the statical analysic
#
# '''* Pandas has two type of data structures
# a)=> Series - its a one dimensional array wirh indexes,it stores a single coloumn or row fo data in a dataframe
# b)=> DataFrame - its a tabular spreadsheet like strctre representing rows each of which contains one or multiple columns
# # A one-D array capable of holding any type of data-series
# # A two-D data structure with columns of potentially different types of data-DataFrame
# '''
# print("-----series-------")
# ser = pd.Series(np.arange(1, 10))
# print(ser)
# print(type(ser))
# print("---or_series---")
# ser2 = pd.Series(np.arange(1, 10), index=[10, 20, 30, 40, 50, 60, 70, 80, 90])
# print(ser2)
# print("----dict series---")
# data = {'a': 0., 'b': 1., 'c': 2.}
# s = pd.Series(data)
# print(s)
# print("----or dict series----")
# data = {'a': 0., 'b': 1., 'c': 2.}
# s = pd.Series(data, index=['b', 'c', 'd', 'a'])
# print(s)
# print("----series scaler---")
# s = pd.Series(5, index=[0, 1, 2, 3])
# print(s)
# print(s[:3])
# print(s[0])
# print(s[['a', 'c', 'd']])
print("---------dataframe---------")
newdf = pd.DataFrame(np.random.randn(100, 5))
print(newdf)
print(newdf.dtypes)
print(newdf.head(5))
print(newdf.describe())
newdf[0][0] = "python_all_concept"
print(newdf.head(5))
print(newdf.dtypes)
print("-------")
print(newdf.index)
print(newdf.columns)
print("--------")
print(newdf.to_numpy())

# print("----------sorting of index----------")
# print(newdf.sort_index(axis=0, ascending=False))
# print(newdf.sort_index(axis=1, ascending=False))
# # print(newdf.sort_values(axis=1)
#
# print("------copy Dataframe-------")
# newdf2 = newdf
# newdf2[0][0] = 255
# print(newdf)
#
# newdf3 = newdf.copy()
# newdf3[0][1] = 10000
# print(newdf)
# print(newdf3)
# # whenever we set a value like this we use
# print("-----.loc-----")
# # .loc
# newdf.loc[0, 0] = 500
# print(newdf.head(5))
#
# newdf.columns = list("ABCDE")
# print(newdf.head(5))
# newdf.loc[2, 'C'] = 786
# print(newdf)
#
# # we can create a dataframe using  .loc => which is used when we want to acess the dataframe through its name
# print(newdf.loc[[1, 2], ['C', 'D']])  # if we want to create a new type of newdf we use the expression shown in nxt line
# # newdf = newdf.loc[[1, 2], ['C', 'D']]
# # printf(newdf)
# print("---- full loc -----")
# # if we want to take all the rows or columns
# print(newdf.loc[:, ['C', 'D']])
# print(newdf.loc[[1, 2], :])
# print(newdf.head(5))
# print("--------boolean statements-----------")
# print(newdf.loc[(newdf['A'] < 0.3) & (newdf['C'] > 0.1)])
#
# print("-----.iloc-----")
# # iloc => if we to access the Dataframe through its index whatever the name is
# print(newdf.head(4))
# print(newdf.iloc[0, 3])
# print(newdf.iloc[[1, 2], [1, 2]])
#
# print("-----drop-----")
# # if we want to drop one column or index
# print(newdf.head(5))
# newdf = newdf.drop('E', axis=1)
# # newdf = newdf.drop('E', axis=1,inplace = True) this will be our orignal newdf after droping row or column
# newdf2 = newdf.drop([1, 3, 5], axis=0)
# print(newdf2.head(6))
# print(newdf2.reset_index(
#     drop=True))  # .reset_index will reset the index again  # But if we dont choose the drop=true then it will show us the index column repeat 2 times
