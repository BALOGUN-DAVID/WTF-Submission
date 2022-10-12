#!/usr/bin/env python
# coding: utf-8

# In[7]:


#1.Print all elements of a list using for loop

number=[1,2,3,4,5,6,7,8,9]
for i in number:
    print(i)


# In[1]:


#2 A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

year_of_service= int(input("enter year of service "))
salary= float(input("enter your salary "))
if year_of_service > 5:
    net_bonus= salary*0.05
    print(net_bonus)
else:
    print(salary)


# In[4]:


# 3. Take input of age of 3 people by user and determine oldest and youngest among them.

age1=int(input("enter your age "))
age2=int(input("enter your age "))
age3=int(input("enter your age "))
list=[age1,age2,age3]
print("oldest is ", max(list))
print("youngest is ", min(list))


# In[6]:



age1=int(input("enter your age "))
age2=int(input("enter your age "))
age3=int(input("enter your age "))
print()
if (age1 > age2) & (age1 > age3):
    print('person 1 is the oldest')
    if age2 < age3:
        print('person 2 is the youngest')
    else:
        print('person 3 is the youngest')
elif (age2 > age1) & (age2 > age3):
    print('person 2 is the oldest')
    if age1 < age3:
        print('person 1 is the youngest')
    else:
        print('person 3 is the youngest')
else:
    print('person 3 is the oldest')
    if age1< age2:
        print('person 1 is the youngest')
    else:
        print('person2 is the youngest')


# In[7]:


#4 & 5.Ask user to enter marks and print the corresponding grade

marks=int(input("enter your marks: "))
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
elif marks > 80:
    print("A")


# In[1]:


#6. Write a Python script to merge two Python dictionaries
mydict1={"Chinaaza":"Nigeria","Cynthia":"Ghana","Dareen":"Egypt","Crestable":"Kenya"}
print(mydict1)
mydict2={"Chisom":"Nigeria", "Comfort":"Nigeria"}
print(mydict2)
mydict = mydict1.copy()
mydict.update(mydict2)
print(mydict)


# In[ ]:





# In[12]:


#7.  Write a Python program to get the largest number from a list
list = [8,54,70,50,30,35,20,90,67,54,82,21,4,79]
print("The largest number from the list: ", max(list))


# In[6]:


#8. Write a python program to remove a key from a dictionary

clas={"Chinaaza":"Nigeria","Cynthia":"Ghana","Dareen":"Egypt","Crestble":"Kenya"}
print(clas)
if 'Dareen' in clas:
    del clas ['Dareen']
print(clas)


# In[ ]:





# In[ ]:




