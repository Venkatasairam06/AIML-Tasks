#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


# In[20]:


data1 = pd.read_csv("NewspaperData.csv")
data1.head()


# In[21]:


data1.info()


# In[22]:


data1.isnull().sum()


# In[23]:


data1.describe()


# In[24]:


plt.figure(figsize=(6,3))
plt.title("Box plot for Daily Sales ")
plt.boxplot(data1["daily"], vert = False)
plt.show()


# In[25]:


sns.histplot(data1['daily'], kde = True,stat='density')
plt.show()


# In[26]:


plt.figure(figsize=(6,3))
plt.title("Box plot for Daily Sales ")
plt.boxplot(data1["sunday"], vert = False)
plt.show()


# In[27]:


sns.histplot(data1['sunday'], kde = True,stat='density')
plt.show()


# ## Observations
# - There are no missing values
# - The daily column values appears to be right-skewed
# - The sunday column values also appear to be right-skewed
# - There are two outliers in both daily column and also in sunday column as observed from the 

# ### Scatter plot and Correlation Strength 

# In[28]:


x= data1["daily"]
y = data1["sunday"]
plt.scatter(data1["daily"], data1["sunday"])
plt.xlim(0, max(x) + 100)
plt.ylim(0, max(y) + 100)
plt.show()


# In[29]:


data1["daily"].corr(data1["sunday"])


# In[30]:


data1[["daily","sunday"]].corr()


# In[31]:


data1.corr(numeric_only=True)


# ### Observations on Correlation Strength 
# - The relationship between x (daily) and y (sunday) is seen to be linear as seen from scatter plot
# - The correlation is strong and positive with Pearson's correlation coefficient of 0.958154

# ### Fit a Linear Regression Model

# In[32]:


import statsmodels.formula.api as smf
model1 = smf.ols("sunday~daily",data = data1).fit()


# In[33]:


model1.summary()


# ### Interpretation
# - R^2=1-->Perfect fit(all variance explained)
# - R^2=0-->Model does not explain any variance
# - R^2 close to 1-->Good model fit
# - R^2 close to 0-->Poor model fit

# In[38]:


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


# ### Observations from Model Summary
# - The probability(p-value) for intercept (beta_0) is 0.707 > 0.05
# 
# - Therefore the intercept coefficient may not be that much significant in prediction
# 
# - However the p-value for “daily” (beta_1) is 0.00 < 0.05
# 
# - Therefore the beta_1 coefficient is highly signific

# In[40]:


model1.params


# In[50]:


print(f'model t-values:\n{model1.tvalues}\n----------\nmodel p-values: \n{model1.pvalues}')


# In[46]:


{model1.rsquared,model1.rsquared_adj}


# ### Prdict for new data point

# In[47]:


newdata=pd.Series([200,300,1500])


# In[48]:


data_pred=pd.DataFrame(newdata,columns=['daily'])
data_pred


# In[49]:


model1.predict(data_pred)


# In[52]:


pred = model1.predict(data1["daily"])
pred


# In[54]:


data1["Y_hat"] = pred
data1


# In[55]:


data1["residuals"]= data1["sunday"]-data1["Y_hat"]
data1


# In[56]:


mse = np.mean((data1["daily"]-data1["Y_hat"])**2)
rmse = np.sqrt(mse)
print("MSE: ",mse)
print("RMSE: ",rmse)


# In[ ]:




