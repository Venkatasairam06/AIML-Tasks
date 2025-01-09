#!/usr/bin/env python
# coding: utf-8

# In[6]:


def avg_value(*n):
    l = len(n)
    average = sum(n)/l
    return average


# In[8]:


avg_value(10,20,60,100,900,1000)


# In[10]:


greet = lambda name : print(f"Good morning {name}!")


# In[11]:


greet("sairam")


# In[12]:


product = lambda a,b,c : a*b*c


# In[13]:


product(20,30,40)


# In[32]:


s = lambda L : [x for x in L if x%2 ==0]


# In[33]:


my_list = [100,3,9,38,43,56,20]
s(my_list)


# In[34]:


def mean_value(*n):
    num_list = list(n)
    num_list.sort()
    l = len(num_list)
    if l%2 == 0:
        median = (num_list[int(1/2)] + num_list[int((1/2))-1])/2
    else:
        median = num_list[int(1/2)]
    return median


# In[35]:


mean_value(1,2,3,4,5,6,7,8,9,10)


# In[36]:


def median_value(*n):
    num_list = list(n)
    num_list.sort()
    l = len(num_list)
    if l%2 == 0:
        median = (num_list[int(1/2)] + num_list[int((1/2))-1])/2
    else:
        median = num_list[int(1/2)]
    return median


# In[38]:


median_value(1,2,3,4,5,6,7,8,9,10)


# In[ ]:




