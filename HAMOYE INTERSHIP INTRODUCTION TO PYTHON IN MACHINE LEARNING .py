#!/usr/bin/env python
# coding: utf-8

# # Numpy Array- 

# # numpy are datastructures used to handle arrays and matrices to create python list 

# In[1]:


import numpy as np


arr=[6,7,8,9]
print(type(arr))


# In[6]:


a=np.array(arr)
print(type(a))
print(a.shape)
print(a.dtype)

#getting dimension with ndim
print(a.ndim)


# In[14]:


b=np.array([[1,2,3],[4,5,6,]])
print(b)
print(b.shape)


#getting dimension with ndim
print(b.ndim)


# In[21]:


#2 by 3 arrays with  random variables 
np.random.random((2,3))


# In[24]:


#2 by 3 arrays with  zeros variables 
np.zeros((2,3))


# In[29]:


#intra operability array with scalar 
c=np.array([[9.0, 8.3, 7.0], [4.0,3.5,2.0]])
d=np.array([[4.4, 3.2,1.0], [6.0,5.0.1.0]])
pri


# In[31]:


#indexing in array using array for data processing
c=np.array([[9.0, 8.3, 7.0], [4.0,3.5,2.0]])

c[0]


# # INTRODUCTING PANDAS DATA STRUCTURES: INDEXING, SERIES, AND DATA FRAME 

# In[7]:


import pandas as pd 
import numpy as np
days= pd.Series(['Monday','Tuesday','Wednesday','Thursaday','Friday'])
print(days)


# In[8]:


#creating lists with a numpy array 
days_lists= np.array(['Monday', 'Tuesday', 'Wednesday'])
numpy_days= pd.Series(days_lists)
print (numpy_days)


# In[9]:


#using strings as indexes
days = pd.Series(['Monday','Tuesday','Wednesday'],
index=['a', 'b' ,'c'])

#create Series from dictionary 
day1= pd.Series({'a':'Monday', 'b':'Tuesday', 'c':'Wednesday'}) 
print (day1)




# In[10]:


#accessing series 
day1= pd.Series({'a':'Monday', 'b':'Tuesday', 'c':'Wednesday'})
print(day1)

day1[0]= 'Monday'
print(day1[0])

day2[1:]='Tuesday'
print(day2[1:])

day3['c']='Wednesday'
print (day3['c'])


# In[40]:


#pribnting empty dataframe 
print (pd.DataFrame())
Empty_DataFrame 
columns:[]
index:[]


# In[22]:


#creating dataframe from a dict
df_dict1 ={'Country':['Ghana', 'Kenya', 'Nigeri', 'Togo'], 
           'capital':['Accra', 'Nairobi', 'Abuja', 'Lome'],
           'population':[10000, 38000,8500,12000],
           'Age':[60, 70, 80, 75]} 
df=pd.DataFrame(df_dict1, index=[2,4,6,8])
df_list=[['Ghana','Accra',10000,60],
         ['Kenya','Nairobi',38000,70],
         ['Nigeria','Abuja',8500,80],
         ['Togo','Lome',12000,75]],
df1=pd.DataFrame(df_list, columns=['Country',
                                   'capital',
                                   'population',
                                   'Age'], 
                 index=[2,4,6,8])
print(df1)


# In[29]:


#retriving files from Dataframe selecting rows in index 3 using iloc
print(df.iloc[3])



#retriving rows in index 6
print(df.loc[6])

#select capital city 
print(df['capital'])

print(df.at[6,'Country'])

print(df.iat[2,0])


# In[35]:


#getting arithemetric operations in pandas std, min, mean 
print(df['population'].sum())
print(df.mean())
print(df.describe())


# In[43]:


#dropping off missinfg values in pandas using dropna(), fillna(), isnull(), notnull(), repalce()
df_dict2 ={'Name':['James', 'Yemen', 'Caro', np.nan ], 'Profession':['Researcher', 'Artist', 'Doctor', 'Writer'], 'Experience':[12,  12, 8, np.nan], 'Height':[np.nan, 175, 180, 150]}
new_df=pd.DataFrame(df_dict2)
print(new_df)


# In[45]:


#check the cell with missing value as True
print(new_df.isnull())


# In[46]:


#remove rows with missing values 
print(new_df.dropna())


# In[ ]:




