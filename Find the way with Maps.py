#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Write a Python program to triple all numbers of a given list of integers. Use Python map.

nums = [1, 2, 3, 4, 5, 6, 7] 
print("list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of list numbers:")
print(list(result))


# In[ ]:




