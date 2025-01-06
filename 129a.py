#!/usr/bin/env python
# coding: utf-8

# In[1]:


Tup5 = (10,20,1,10,10,30,10)
Tup5.count(10)


# In[12]:


d1 = {"a":1, "b":2, "c":3}
d1


# In[13]:


d2 = dict(A=10, B=20, C=30)
print(d2)


# In[14]:


d3 = dict([("x",1),("y",2),("z",3)])
print(d3)


# In[15]:


print(d1.keys())
print(d1.values())
print(d1.items())


# In[10]:


dir(dict)


# In[5]:


scores = {'Virat':90,'Rohit':100,'Rahul':70,'Hardik':9,'Gill':20,'Jadeja':30,'Siraj':15}
scores


# In[6]:


scores["Ashwin"] = 15
scores


# In[7]:


scores.update({"Jadeja":50})
scores


# In[8]:


scores.update({"Hardik":25,"Rahane":45})
scores


# In[11]:


scores.setdefault("Rahul",60)
scores


# In[16]:


scores.setdefault("Pujara",50)
scores


# In[17]:


scores.popitem()
scores


# In[18]:


scores.get("Siraj")


# In[19]:


list1 = ["A","B","C","D"]
my_dict = dict.fromkeys(list1)
my_dict


# In[22]:


my_dict.update({"A":10,"B":20})
my_dict


# In[23]:


my_dict.update({"C":30,"D":40})
my_dict


# In[25]:


my_dict


# In[ ]:




