#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


# In[32]:


data1 = pd.read_csv("NewspaperData.csv")
data1


# In[33]:


data1.info()


# In[34]:


data1.describe()


# In[35]:


data1.isnull().sum()


# In[36]:


data1.boxplot()


# In[37]:


sns.boxplot(data=data1['daily'],color='blue',width=0.5,orient = 'h')


# In[38]:


plt.hist(data1, bins=6, edgecolor='black')


plt.title('Histogram for Newspaper data')
plt.xlabel('Daily')
plt.ylabel('Count')


plt.show()


# In[39]:


sns.histplot(data=data1['daily'],kde=True,color='green',bins=30)


# In[40]:


plt.scatter(data1["daily"],data1["sunday"])


# In[41]:


data1["daily"].corr(data1["sunday"])


# In[42]:


data1[["daily","sunday"]].corr()


# In[43]:


data1.corr(numeric_only=True)


# In[44]:


plt.figure(figsize=(6,3))
plt.boxplot(data1["daily"], vert = False)


# In[45]:


import seaborn as sns
sns.histplot(data1['sunday'], kde = True,stat='density',)
plt.show()


# In[55]:


x = data1["daily"].values
y = data1["sunday"].values
plt.scatter(x, y, color = "m", marker = "o", s = 30)
b0 = 13.84
b1 =1.33
# predicted response vector
y_hat = b0 + b1*x
 
# plotting the regression line
plt.plot(x, y_hat, color = "g")
  
# putting labels
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[56]:


sns.regplot(x="daily", y="sunday", data=data1)
plt.xlim([0,1250])
plt.show()


# In[ ]:




