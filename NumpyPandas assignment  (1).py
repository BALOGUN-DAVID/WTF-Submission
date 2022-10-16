#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[ ]:


#PANDAS IN-BUILT METHODS


# In[20]:


#Number 1 read_csv()
#helps read a comma-separated values (csv) file into a Pandas DataFrame
data=pd.read_csv('C:\\Users\\HP\\Downloads\\CompositionOfFoods_DataDictionary.csv') #import csv data set as "data" 
#download from the internet
# open downloads, select the file and click copy path from the 'Home' menu, paste path in the 


# In[51]:


#Number 2 head(n)
# displays the first n rows in a data frame
data.head(5)


# In[21]:


#Number 3 dataframe.info
#This is used to get a quick summary of the dataset
data.info


# In[22]:


#Number 4 Dtypes
# This shows the data type of each column
data.dtypes


# In[23]:


#Number 5 Data size and shape
#shape displays the nuber of rows and columns
data.shape


# In[24]:


#size displays the number of rows multiplied by the number of column
data.size


# In[25]:


#Number 6 describe()
#This will do a quick statistical summary for every numerical column
data.describe()


# In[26]:


#Number 7 sample()
#This allows you to select values randomly from a Series or DataFrame
data.sample(n=8)


# In[27]:


#Number 8 isnull()
# to identify missing values
data.isnull()


# In[29]:


#Number 9 isna()
#returns a dataframe filled with boolean values with true indicating missing values.
data.isna().any()


# In[38]:


#Number 10 nunique()
#counts the number of unique entries over columns or rows
data.nunique()


# In[42]:


#Number 11 Index()
#searches for a given element from the start of the list and returns the lowest index where the element appears
data.index


# In[45]:


#Number 12 columns()
#Returns the column names
data.columns


# In[47]:


#Number 13 memory_usage() 
#returns how much memory each column uses in bytes
data.memory_usage()


# In[49]:


#Number 14 nsmallest(n,column name) n is the number of observations
#finds the observations with the smallest value
data.nsmallest(4, 'Character length')


# In[50]:


#Number 15 nlargest(n, column name)
#finds the observations with the Largest value.
data.nlargest(4,'Character length')


# In[52]:


#Number 16 tail(n)
#returns the last n rows in a data set
data.tail(4)


# In[60]:


#Number 17 loc[:]
#displays a group of rows and columns in a dataset, a slice of the dataset, as per requirement
data.loc[0:5,["Description", "Required?", "Acceptable values"]]


# In[62]:


#Number 18 sort_values()
#is used to sort columns by values in ascending or descending order.
data.sort_values(by="Character length")


# In[63]:


#Number 19 drop_duplicates()
#returns a DataFrame with duplicate rows removed
data.drop_duplicates()


# In[65]:


#Number 20 replace(old value, new value)
# It replaces the values of a column
data.replace(120, 20)


# In[24]:


#NUMPY
import numpy as np

data_1= (3,4,5,32,67,7,9,99,66,77,55,66,777,98,38,5,444,94,85,75,43,10,44,50,31,23,13,23,34,14,554,40,59,44,42,)


# In[25]:


#Number 1 .random.randint
# creates random integers in a specific range
np.random.randint(5, size=9)


# In[26]:


#Number 2. random.random
#creates random floats between 0 and 1
np.random.random(10)


# In[28]:


#Number 3 Np.random.randn() 
#is used to create a sample from a standard normal distribution
print(np.random.randn(100).mean())
print(np.random.randn(100).std())


# In[33]:


#Number 4 np.zeros np.ones
# create a matrix with zeros or ones 
np.zeros(8)
np.ones((10,10))


# In[35]:


#Number 5 np.eye
#to create an identity matrix is a square matrix (nxn) that has ones on the diagonal and zeros on every other position
np.eye(5)


# In[36]:


#Number 6 np.arange
#is used to create arrays with evenly spaced sequential values in a specified interval
np.arange(5)


# In[38]:


#Number 7 np.full()
#create an array that has the same value at every position
np.full ((3,10),7)


# In[42]:


#Number 8 ravel()
#flattens the array (i.e. convert to a 1-dimensional array)
F=np.random.randint(5, size=(3,4)) #create a 2d matrix "F"
print(F)
print(F.ravel()) #flatten the 2d matrix "F"


# In[45]:


#Number 9 reshape()
#it reshapes an array that is flat, that is from 1 dimension to 2d
F.reshape(-1,4)


# In[46]:


#Number 10 transpose()
#Transposing a matrix is to switch rows and columns.
F.transpose()


# In[48]:


#Number 11 vsplit()
#Splits an array into multiple sub-arrays vertically.
np.vsplit(F, 3)


# In[50]:


#Number 12 hsplit()
#It is similar to vsplit but works horizontally.
np.hsplit(F,2)


# In[64]:


#Number 13 concatenate
#combine arrays
a= np.array([1,2,3,4,5])
b= np.array([6,7,8,9,10])
c= np.array([11,12,13,14,15])
np.concatenate((a,b,c))


# In[65]:


#Number 14 vstack()
#It is used to stack arrays vertically (rows on top of each other).
np.vstack((a,b,c))


# In[66]:


#Number 15 hstack()
#similar to vstack but stacks horizontally
c=np.array([11,12,13,14])
np.hstack((a,b,c))


# In[71]:


#Number 16 det()
#Returns the determinant of a matrix.
D= np.random.randint(5, size=(3,3))
np.linalg.det(D)


# In[72]:


#Number 17 Inv()
#Calculates the inverse of a matrix.
np.linalg.inv(D)


# In[73]:


#Number 18 Eig
#Computes the eigenvalues and right eigenvectors for a square matrix.
np.linalg.eig(D)


# In[75]:


#Number 19 dot(Dot
#Calculates the dot product of two vectors which is the sum of the products of elements with regards to their position)
np.dot(a,b)


# In[79]:


#Number 20 Matmul
#It performs matrix multiplication.
d= ([[1,2],[3,4]])
e=([[5,6],[7,8]])
np.matmul(d,e)


# In[ ]:




