#!/usr/bin/env python
# coding: utf-8

# In[1]:


#If you run the lab locally using Anaconda, you can load the correct library and versions by uncommenting the following:
#install specific version of libraries used in lab
#! mamba install pandas==1.3.3
#! mamba install numpy=1.21.2


# In[2]:


import pandas as pd
import matplotlib.pylab as plt


# This is a note for me. This was my first method of importing my data and adding the header. I will aslo try another method.

# In[11]:


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


# In[12]:


jos_data = pd.read_csv("C:/data/auto.csv", names = headers)


# In[13]:


jos_data.head()


# In[8]:


jos_data.tail()


# This is my second method

# In[15]:


j_data = pd.read_csv("C:/data/auto.csv")


# In[16]:


j_data.head()


# In[17]:


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


# In[19]:


joe_data = pd.read_csv("C:/data/auto.csv", names = headers)


# In[20]:


joe_data.head()


# In[21]:


import numpy as np


# In[23]:


# replace "?" to NaN
joe_data.replace("?", np.nan, inplace = True)
joe_data.head(5)


# In[24]:


missing_data = joe_data.isnull()
missing_data.head(5)


# In[25]:


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")  


# I have 7 columns with missing values. But I will take them one after the other. First, I am replacing the missing values for normalized-losses with mean

# In[27]:


avg_norm_loss = joe_data["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)


# In[29]:


joe_data["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)


# In[30]:


joe_data.head()


# Number 2: Next I am replaicng for Bore column with the mean as well

# In[32]:


avg_bore=joe_data['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)


# In[33]:


joe_data["bore"].replace(np.nan, avg_bore, inplace=True)


# Number 3: next I am replacing the missing values for stroke with the mean

# In[34]:


avg_stroke=joe_data['stroke'].astype('float').mean(axis=0)
print("Average of stroke:", avg_stroke)


# In[35]:


joe_data["stroke"].replace(np.nan, avg_stroke, inplace=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




