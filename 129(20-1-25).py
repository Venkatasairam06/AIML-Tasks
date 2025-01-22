#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import numpy as np


# In[6]:


df = pd.read_csv("universities.csv")
df


# In[7]:


df.sort_values(by="GradRate",ascending=True)


# In[8]:


df.sort_values(by="GradRate",ascending=False)


# In[10]:


df[df["GradRate"]>=95]


# In[11]:


df[df["SAT"]>=95]


# In[12]:


df[(df["GradRate"]>=80) & (df["SFRatio"]<=12)]


# In[20]:


sal = pd.read_csv("Salaries.csv")
sal


# In[21]:


sal[["salary"]].groupby(sal["rank"]).mean()


# In[22]:


sal[["salary","phd","service"]].groupby(sal["rank"]).mean()


# In[ ]:





# In[ ]:





# In[ ]:




