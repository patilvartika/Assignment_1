#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Write a Python program to square the elements of a list using map() function.

def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
print("List: ",nums)
result = map(square_num, nums)
print("Square the elements of the list:")
print(list(result))


# In[ ]:




