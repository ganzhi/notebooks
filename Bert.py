#!/usr/bin/env python
# coding: utf-8

# In[1]:


from transformers import pipeline


# In[2]:


unmasker = pipeline('fill-mask', model='bert-large-uncased')


# In[3]:


unmasker("Hello I'm a [MASK] model.")


# In[ ]:




