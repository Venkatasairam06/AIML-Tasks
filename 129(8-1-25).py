#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = 6
if num % 2 == 0:
    print("even")
else:
    print("odd")


# In[2]:


num = 7
if num % 2 == 0:
    print("even")
else:
    print("odd")


# In[5]:


x = 10
result = "Positive" if x > 0 else "Negative"
print(result)


# In[6]:


age = 18
Category = "Adult" if age >= 18 else "Minor"
print(Category)


# In[8]:


num = 0
result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(result)


# In[10]:


L = [1,9,2,10,56,89]
[2*x for x in L]


# In[11]:


[x for x in L if x%2 == 0]


# In[12]:


d1 = {'Ram':[70,71,98,100],'John':[56,98,67,72]}
d1


# In[13]:


{k:sum(v)/len(v) for k,v in d1.items()}


# In[14]:


def mean_value(given_list):
       total = sum(given_list)
       average_value = total/len(given_list)
       return average_value


# In[15]:


L = [1,2,3,4,5,6,7,8,9,10]
mean_value(L)


# In[ ]:




