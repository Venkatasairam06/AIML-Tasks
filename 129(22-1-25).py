#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


df = pd.read_csv("universities.csv")
df


# In[3]:


df.sort_values(by="GradRate",ascending=True)


# In[4]:


df.sort_values(by="GradRate",ascending=False)


# In[5]:


df[df["GradRate"]>=95]


# In[6]:


df[df["SAT"]>=95]


# In[7]:


df[(df["GradRate"]>=80) & (df["SFRatio"]<=12)]


# In[8]:


sal = pd.read_csv("Salaries.csv")
sal


# In[9]:


sal[["salary"]].groupby(sal["rank"]).mean()


# In[10]:


sal[["salary","phd","service"]].groupby(sal["rank"]).mean()


# In[11]:


sal[["phd"]].groupby(sal["rank"]).mean()


# In[12]:


df = pd.read_csv("universities.csv")
df


# In[13]:


#mean value of SAT score
np.mean(df["SAT"])


# In[14]:


#median value of SAT score
np.median(df["SAT"])


# In[15]:


#find the variance
np.var(df["SFRatio"])


# In[16]:


df.describe()


# In[17]:


#Visualize the GradRate using Histogram
import matplotlib.pyplot as plt
import seaborn as sns


# In[20]:


plt.figure(figsize=(6,3))
plt.title("Graduation Rate")
plt.hist(df["GradRate"])


# In[ ]:




