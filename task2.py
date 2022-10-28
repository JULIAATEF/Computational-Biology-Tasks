#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyopenms import *


# In[2]:


seq = AASequence.fromString("VAKA")


# In[3]:


seq.getMonoWeight()


# In[14]:


for aa in seq:
    print(aa.getMonoWeight())


# In[15]:


sum=0
for aa in seq:
        sum +=aa.getMonoWeight()
print(sum)


# In[ ]:





# In[ ]:





# In[ ]:




