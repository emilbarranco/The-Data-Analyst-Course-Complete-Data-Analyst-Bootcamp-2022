#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Lecture on Linear Algebra

# Matrices - A matrix is a collection of numbers ordered in rows and columns (2 dimensions). Example:

# A = 
# [5 12 6]
# [3 0 14]

# Each value is an "element".
# The matrix above is composed of 2 rows and 3 columns. A is a 2 by 3 matrix.
# Rows & Columns are the the two dimensions of matrices.
# Can only contain numbers, symbols and expressions.


# In[2]:


# Lecture on Vectors and Scalars

# Scalars

# All numbers we lnow from Algebra are referred to as scalars in linear algebra.
# Scalars contain 1 row and 1 column, meaning, 1 element. (0 dimensions)

# Example: [15]; [1]; [2]; [-5]

# Vectors

# They sit between Scalars and Matrices (1 dimension).
# A vector is practically the simplest linear algebraic object.
# There are two types of vectors, column and row vectors:

# [3 4 5 6] - row (length = 4)

# [5] - column (length = 3)
# [2]
# [4]


# In[3]:


# Lecture on Arrays in Python


# In[4]:


# Import the relevant libraries
import numpy as np


# In[5]:


# Declaring scalars, vectors and matrices.


# In[6]:


# Scalars

s = 5
s


# In[9]:


# Vectors

v = np.array([5, -2, 4])
v


# In[11]:


# Matrices

m = np.array([[5, 12, 6], [-3, 0, 14]])
m


# In[13]:


# Data Types


# In[14]:


type(s)


# In[15]:


type(v) # 1-dimensional array


# In[16]:


type(m) # 2-dimensional array


# In[17]:


s_array = np.array(5) # another way to create a scalar in numpy
s_array


# In[18]:


type(s_array)


# In[19]:


# Data Shapes

m.shape # 2 rows 3 columns


# In[20]:


v.shape


# In[22]:


v.reshape(1, 3)


# In[23]:


v.reshape(3, 1)


# In[24]:


s_array.shape


# In[25]:


# What are Tensors.

# Tensors are simply a generalization of the concepts previously discussed. 

# Scalars (1x1) -------> Tensor Rank 0
# Vectors(1xm, mx1) -------> Tensor Rank 1
# Matrices(mxn) -------> Tensor Rank 2

# A Tensor (k x m x n) is a collection of matrices.


# In[ ]:


# Creating a Tensor out of 2 matrices.

