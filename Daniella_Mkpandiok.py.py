#!/usr/bin/env python
# coding: utf-8
#1 Print all elements of a list using for loop

# In[9]:


numbers = [1, 3, 12, 45, "sex", "gender"]
for items in numbers:
    print(items)

#2 A company decided to give bonus of 5% to employee if his/her year of service is more than 5
years. Ask user for their salary and year of service and print the net bonus amount.
# In[7]:


year_of_service = int(input("enter the year of service"))
salary = float(input("input your salary"))
if year_of_service > 5:
    net_bonus = salary * 0.05
    print(net_bonus)
else:
    print(salary)

#3 Take input of age of 3 people by user and determine oldest and youngest among them.
# In[14]:


age_1 =  int(input("Enter your age"))
age_2 =  int(input("Enter your age"))
age_3 =  int(input("Enter your age"))
if (age_1 >= age_2) and (age_1 >= age_3):
    print("User_1 is the oldest")
elif age_2 >= age_1 and age_2 >= age_3:
    print("User_2 is the oldest")
elif age_3 >= age_1 and age_3 >= age_2:
    print("User_3 is the oldest")
else:
    print("none is the oldest")

#4 A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
# In[16]:


marks = int(input("Enter your marks"))
if marks < 25:
    print("F")
elif 25 < marks <= 45:
    print("E")
elif 45 < marks <= 50:
    print("D")
elif 50 < marks <= 60:
    print("C")
elif 60 < marks <= 80:
    print("B")
else:
    print("A")

#5 Write a Python script to merge two Python dictionaries
# In[17]:


Dictionary1 = {"Oyo" :"Ibadan", "Ogun":"Abeokuta", "Gongola" :"Yola" }
Dictionary2 = {"Ibadan":"Oluyole", "Abeokuta":"Abeokuta South"}
Dictionary1.update(Dictionary2)
print(Dictionary1)

#6 Write a python program to get the largest number from a list
# In[23]:


numbers = [2, 6, 8, 10, 15, 50]
largest_number =max(numbers)
print(largest_number)

#7 Write a python program to remove a key from a dictionary
# In[31]:


dict_1 = {"Oyo" : "Ibadan","Crossriver" : "Calabar", "Plateau" : " Jos"}
dict_2 = dict_1.popitem()
print("dict_1 after poping",dict_1)
print("dict_2 key that was pop", dict_2)


# In[ ]:




