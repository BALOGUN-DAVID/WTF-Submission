#!/usr/bin/env python
# coding: utf-8

# In[4]:


print('Enter your grade marks')
grade_marks = int(input())
if grade_marks<25:
    print('grade =', 'F')
elif grade_marks<=45:
    print('grade =', 'E')
elif grade_marks<=50:
    print('grade =', 'D')
elif grade_marks<=60:
    print('grade =', 'C')
elif grade_marks<=80:
    print('grade =', 'B')
else:
    print('A')


# In[5]:


d1 = {'a': 20, 'b': 30, 'o': 40}
d2 = {'p': 50, 'g': 60, 'h': 70}
d = d1.copy() 
d.update(d2)
print(d)


# In[6]:


print('Enter salary')
salary = int(input())
print('Enter years of service')
service_yrs = int(input())
if (service_yrs>5):
    print('Bonus is', 0.05*salary)
else:
    print('No Bonus')


# In[7]:


even_nums = []

odd_nums = []

for i in range(1,101):

    if i % 2 == 0:

        even_nums.append(i)

    else:

        odd_nums.append(i)
        
print(even_nums)

print(" ")

print(odd_nums)
        


# In[8]:


fruits = ['mango', 'grape', 'orange', 'apple', 'watermelon', 'banana']
for a in fruits:
    print(a)


# In[9]:


list = {2, 8, 30, 60, 200}
print(max(list))


# In[10]:


myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)


# In[ ]:




