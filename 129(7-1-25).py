#!/usr/bin/env python
# coding: utf-8

# In[1]:


s1 = {1,2,3,4}
s2 = {3,4,5,6}


# In[2]:


s1 | s2


# In[3]:


s1 = {1,2,3,4}
s2 = {3,4,5,6}


# In[4]:


s1 & s2


# In[5]:


s1.intersection(s2)


# In[6]:


s1 = {2,3,5,6,7}
s2 = {5,6,7}


# In[7]:


s1 - s2


# In[8]:


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}


# In[9]:


s1.symmetric_difference(s2)


# In[10]:


s2.symmetric_difference(s1)


# In[11]:


str1 = "Welcome to aiml class"
print(str1)
str2 = 'We started with python'
print(str2)
str3 = '''This is an awesome class'''
print(str3)


# In[12]:


print(type(str1))
print(type(str2))
print(type(str3))


# In[16]:


str4 = '''He said, "It's awesome!"'''
str4


# In[18]:


print(str1)
str1[5:10]


# In[19]:


dir(str)


# In[20]:


print(str1)
str1.split()


# In[21]:


reviews = ["The product is awesome","Great Service"]
joined_string = ' '.join(reviews)
joined_string


# In[24]:


str5 = "   Hello,How are you?"
print(str5)
str5.strip()


# In[ ]:




