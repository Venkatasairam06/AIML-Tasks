#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[5]:


data.info()


# In[6]:


print(type(data))
print(data.shape)
print(data.size)


# In[7]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[8]:


data1.info()


# In[9]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[10]:


data1[data1.duplicated(keep = False)]


# In[11]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[12]:


data1.rename({'Solar.R': 'Solar'}, axis=1, inplace = True)
data1


# In[13]:


data1.info()


# In[15]:


data1.isnull().sum()


# In[16]:


cols = data1.columns
colors = ['black', 'blue']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[17]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean of Ozone: ", mean_ozone)


# In[21]:


data['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[23]:


print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[24]:


data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[25]:


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


# In[26]:


sns.violinplot(data=data1["Ozone"], colors='lightgreen')


# In[40]:


plt.figure(figsize=(6,2))
plt.boxplot(data1["Ozone"], vert= False)


# In[37]:


data1["Ozone"].describe()


# In[41]:


mu = data1["Ozone"].describe()[1]
sigma = data1["Ozone"].describe()[2]

for x in data1["Ozone"]:
    if ((x < (mu - 3*sigma)) or (x > (mu + 3*sigma))):
        print(x)


# In[34]:


import scipy.stats as stats
plt.figure(figsize=(8, 6))
stats.probplot(data1["Ozone"], dist="norm", plot=plt)
plt.title("Q-Q Plot for Outlier Detection", fontsize=14)
plt.xlabel("Theoretical Quantiles", fontsize=12)


# In[ ]:




