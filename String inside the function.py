#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to reverse a string.

def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))


# In[ ]:




