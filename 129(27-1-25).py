#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[17]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[18]:


data.info()


# In[19]:


print(type(data))
print(data.shape)
print(data.size)


# In[20]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[21]:


data1.info()


# In[22]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[23]:


data1[data1.duplicated(keep = False)]


# In[24]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[25]:


data1.rename({'Solar.R': 'Solar'}, axis=1, inplace = True)
data1


# In[26]:


data1.info()


# In[27]:


data1.isnull().sum()


# In[28]:


cols = data1.columns
colors = ['black', 'blue']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[29]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean of Ozone: ", mean_ozone)


# In[30]:


data['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[31]:


print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)]


# In[32]:


data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# Detection of outliers in the columns

# Method1: Using histograms and box plots

# In[45]:


fig, axes = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [1, 3]})

sns.boxplot(data=data1["Ozone"], ax=axes[0], color='blue', width=0.5, orient = 'h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Ozone levels")
 
sns.histplot(data1["Ozone"], kde=True, ax=axes[1], color='green', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone levels")
axes[1].set_ylabel("Frequency")

plt.tight_layout()

plt.show()


# In[ ]:




