#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math # Introduction to Modules


# In[ ]:


math.sqrt(16)


# In[ ]:


from math import sqrt


# In[ ]:


sqrt(256)


# In[ ]:


import math as m # Importing module while renaming it.


# In[ ]:


m.sqrt(36)


# In[ ]:


# Introduction to NumPy and Pandas


# In[ ]:


# NumPy ------

# The fundamental package for scientific computing
# with Python.

# Using NumPy gets you as close as possible to
# straight mathematics.

# Pandas ------

# It needs the computational power and abilities of 
# NumPy to perform its computations.

# It allows you to focus more on your analytic task 
# and less on the underlying mathematical computations.


# In[4]:


# Starting the usage of these libraries here.

import numpy as np


# In[5]:


np.__version__


# In[6]:


import pandas as pd


# In[7]:


pd.__version__


# In[9]:


list_1 = [1, 2]
list_1


# In[10]:


list_2 = [34, 35]
list_2


# In[11]:


list_1.extend(list_2)


# In[12]:


list_1

