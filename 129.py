#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd


# In[19]:


import numpy as np


# In[20]:


l1=[77,62,88,90]


# In[21]:


l2=[55,81,76,72]


# In[22]:


l3=[80,69,75,94]


# In[23]:


l4=[83,60,90,95]


# In[24]:


marks=[l1,l2,l3,l4]


# In[25]:


marks


# In[29]:


df=pd.DataFrame(marks,columns=['English','Maths','Physics','Chemistry'],index=['Rahul','Rohit','Riya','Sita'])


# In[30]:


print(df)


# In[31]:


csvf=df.to_csv(r"C:\Users\MRUH\Desktop\129\ML_LAB.csv")


# In[ ]:




