#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


s = [20,15,10,25,30,35,28,150,120]
scores = pd.Series(s)
scores


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


plt.boxplot(scores,vert=False)


# In[13]:


s = [20,15,10,25,30,35,28,150,120,66,]
scores = pd.Series(s)
scores


# In[14]:


plt.boxplot(scores,vert=False)


# In[16]:


df = pd.read_csv("universities.csv")
df


# In[17]:


plt.figure(figsize=(6,2))
plt.title("Box plot for SAT Score")
plt.boxplot(df["SAT"],vert=False)


# In[ ]:




