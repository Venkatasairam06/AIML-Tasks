#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np


# In[6]:


cars = pd.read_csv("Cars.csv")
cars.head()


# In[7]:


cars = pd.DataFrame(cars,columns=["HP","VOL","SP","WT","MPG"])
cars.head()


# #### Description of columns
# - MPG: Milege of the car(Mile per Gallon)(This is T-column to be predicted)
# - HP:Horse Power of the car(X1 column)
# - VOL:Volume of the car(size)(X2 column)
# - SP: Top speed of the car(Miles per Hour)(X3 column)
# - WT:Weight of the car(pounds)(X4 column)

# #### Assumptions in Multi Linear Regression
# - **1.Linearity:** The relationship between the predictors(X) and the response(Y) is linear.
# - **2.Independence:** Observations are independent of each other
# - **3.Homoscedasticity:** The residuals (Y-Y_hat) exhibit constant variance at levels of the predictor.
# - **4.Normal Distribution of Errors:** The residuals of the model are normally diastributed.
# - **5.NO Multicolinearity:** The independent variables should not be too highly correlated with each other

# In[8]:


cars.info()


# In[9]:


cars.isna().sum()


# ### Observations about info(),missing values
# - There are no missing values
# - There are 81 observations(81 different cars data)
# - The data types of the columns are also relevant and valid

# In[12]:


# Create a figure with two subplots(one above the other)
fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

# Creating a boxplot
sns.boxplot(data=cars, x='HP', ax=ax_box, orient='h')
ax_box.set(xlabel='') # Remove x label for the boxplot

# Creating a histogram in the same x-axis
sns.histplot(data=cars, x='HP', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')

# Adjust Layout
plt.tight_layout()
plt.show()


# In[13]:


# Create a figure with two subplots(one above the other)
fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

# Creating a boxplot
sns.boxplot(data=cars, x='VOL', ax=ax_box, orient='h')
ax_box.set(xlabel='') # Remove x label for the boxplot

# Creating a histogram in the same x-axis
sns.histplot(data=cars, x='VOL', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')

# Adjust Layout
plt.tight_layout()
plt.show()


# In[14]:


# Create a figure with two subplots(one above the other)
fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

# Creating a boxplot
sns.boxplot(data=cars, x='SP', ax=ax_box, orient='h')
ax_box.set(xlabel='') # Remove x label for the boxplot

# Creating a histogram in the same x-axis
sns.histplot(data=cars, x='SP', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')

# Adjust Layout
plt.tight_layout()
plt.show()


# In[15]:


# Create a figure with two subplots(one above the other)
fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

# Creating a boxplot
sns.boxplot(data=cars, x='WT', ax=ax_box, orient='h')
ax_box.set(xlabel='') # Remove x label for the boxplot

# Creating a histogram in the same x-axis
sns.histplot(data=cars, x='WT', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')

# Adjust Layout
plt.tight_layout()
plt.show()


# In[16]:


# Create a figure with two subplots(one above the other)
fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

# Creating a boxplot
sns.boxplot(data=cars, x='MPG', ax=ax_box, orient='h')
ax_box.set(xlabel='') # Remove x label for the boxplot

# Creating a histogram in the same x-axis
sns.histplot(data=cars, x='MPG', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')

# Adjust Layout
plt.tight_layout()
plt.show()


# ### Observations from boxplot and histograms
# - There are some extreme values (outliers) observed in towards the right tail of SP and HP distributions.
# - In VOL and WT columns, a few outliers are observed in both taills of their distributins.
# - The extreme values of cars data may have come from the specially designed nature of cars
# - As this is multi-dimensional data, the outliers with respect to spatial dimensions may have to be considered while building the regression model

# #### Checking for duplicated rows

# In[17]:


cars[cars.duplicated()]


# #### Pair plots and Correlation Coefficients

# In[18]:


# Pair plot
sns.set_style(style='darkgrid')
sns.pairplot(cars)


# In[ ]:




