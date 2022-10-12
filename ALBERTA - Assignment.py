#!/usr/bin/env python
# coding: utf-8

# # ALBERTA ADU

# 1) Print all elements of a list using for loop

# In[1]:


grocery_lists = ['Milo', 'Cerelac', 'Cheese', 'Eggs']
for grocery_list in grocery_lists:
    print(grocery_list)


# 2) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

# In[33]:


salary = int(input("Please enter your salary: "))
year_of_service = int(input("Please enter the number of years of service: "))

if year_of_service > 5:
    net_bonus = (0.05 * salary) + salary
else:
    net_bonus = salary
print(net_bonus)


# 3) Take input of age of 3 people by user and determine oldest and youngest among them.

# In[5]:


age1 = input("Please enter your age : ")
age2 = input("Please enter your age : ")
age3 = input("Please enter your age: ")
if (age1 > age2) & (age1 > age3):
    print('Person 1 is the oldest')
    if age2 < age3:
        print('Person 2 is the youngest')
    else:
        print('Person 3 is the youngest')
elif (age2 > age1) & (age2 > age3):
    print('Person 2 is the oldest')
    if age1 < age3:
        print('Person 1 is the youngest')
    else:
        print('Person 3 is the youngest')
else:
     print('Person 3 is the oldest')
     if age1 < age2:
         print('Person 1 is the youngest')
     else:
        print('Person 2 is the youngest')
    


# 4) A school has following rules for grading system: 
#    - a. Below 25 - F 
#    - b. 25 to 45 - E 
#    - c. 45 to 50 - D 
#    - d. 50 to 60 - C 
#    - e. 60 to 80 - B 
#    - f. Above 80 - A

# 5) Ask user to enter a mark and print the corresponding grade.

# In[21]:


marks = int(input("Please enter your marks: "))
if marks > 80:
    print("A")
elif marks >= 60 & marks <= 80:
    print("B")
elif marks >= 50 & marks < 60:
    print("C")
elif marks >= 45 & marks < 50:
    print("D")
elif marks >= 25 & marks < 45:
    print("E")
elif marks < 25:
    print("F")

    


# 6) Write a Python script to merge two Python dictionaries.

# In[23]:


dict_A = {'Alberta': 21, 'Cindy': 18, 'Mark': 25}
dict_B = {'Ghana': 'Accra', 'UAE': 'Dubai', 'Canada': 'Toronto'}
dict_C = dict_A.copy()
dict_C.update(dict_B)
print(dict_C)


# 7) Write a python program to get the largest number from a list

# In[27]:


list = [25, 30, 555, 100]
for x in list:
    if x > list[0]:
        list[0] = x
print(list[0])


# 8) Write a python program to remove a key from a dictionary

# In[28]:


dict_A = {'Africa': ['Egypt', 'Kenya'], 'Europe': ['France', 'Germany'], 'Asia': ['China', 'Maldives']}
dict_A


# In[29]:


dict_A.pop('Asia')
dict_A

