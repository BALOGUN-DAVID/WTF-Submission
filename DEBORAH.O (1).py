#!/usr/bin/env python
# coding: utf-8

# # print all elements of a list using for loop

# In[1]:


myList = ['James', 'Otobong', 'Temitayo', 'Blessing', 'Benard', 'Anthony', 'Isangha', 'Hilary', 'Opeoluwa', 'Victory']

for student in myList:
    print(student)


# # using range(1,101), make two list, one containing all even numbers and other containing all odd numbers
# 
# 

# In[21]:


lowerRange = 1
upperRange = 101
i = 2

print("Even numbers between", lowerRange, "and", upperRange, "are:")

for Z in range(lowerRange, upperRange + 1):
      if Z > 1:
            if (Z % i) == 0:
                print(Z)


# In[20]:


lowerRange = 1
upperRange = 101
i = 2

print("Odd numbers between", lowerRange, "and", upperRange, "are:")

for Z in range(lowerRange, upperRange + 1):
      if Z >= 1:
            if (Z % i) != 0:
                print(Z)


# # A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount

# In[41]:


target = 5
def bonusCalc(sal,year):
    if year > target:
        netBonus = sal*0.05
        print('Your net bonus is: ', netBonus)
        return netBonus
    else:
        print('Sorry, but at this time, you are not qualified for bonus')
    


# In[42]:


salary = input('How much is your salary')
Year = input('how long is your year of service in this organization')

bonusCalc(int(salary),int(Year))


# # Take Input of age 3 people by user and determine oldest and youngest among them

# In[52]:


def ageRange(age1,age2,age3):
    if (age1 > age2) & (age1 > age3):
        print('the oldest is the first person')
        if age2 < age3:
                print('the youngest is the second person')
        else:
                print('the youngest is the third person')
                
    elif (age2 > age1) & (age2 > age3):
        print('the oldest pesron is the second person')
        if age1 < age3:
                print('the youngest is the first person')
        else:
                print('the youngest is the third person')
    else:
        print('the oldest is the third person')
        if age1 < age2:
                print('the youngest is the first person')
        else:
                print('the youngest is the second person')
        
    


# In[72]:


firstPerson = input('how old are you? ')
secondPerson = input('how old are you? ')
thirdPerson = input('how old are you? ')

ageRange(int(firstPerson), int(secondPerson), int(thirdPerson))


# # A school has following rules for grading system:
#     Below 25 -F
#     25 to 45 -E
#     45 to 50 -D
#     50 to 60 -C
#     60 to 80 -B
#     Above 80 -A

# In[33]:


def scoreGrade(score):
    if score > 80:
        print("your grade is 'A'")
    elif score >60 and score <=80:
        print("your grade is 'B'")
    elif score >50 and score <=60:
        print("your grade is 'C'")
    elif score >45 and score <=50:
        print("your grade is 'D'")
    elif score >25 and score <=45:
            print("your grade is 'E'")

    else: 
        print("your grade is 'F'")
#return grd     


# In[34]:


score = input('what was your score')  
scoreGrade(int(score))


# # Write a Python script to merge two python dictionaries

# In[57]:



dict2 = {'CAD':1.52, 'EUR':1.14, 'Tola':4, 'Temmy':40}

dict1.update(dict2)
print(dict1)dict1 = {'NGN':470, 'GBP':0.99, 'MXN':20.1, 'ZAR':17.99, 'ZMK':15830, 'GHS':10.5, 'DEM':1.99, 'USD':1}


# # Write a Python program to remove a key from a dictionary

# In[64]:


mergedDict = {'NGN': 470, 'GBP': 0.99, 'MXN': 20.1, 'ZAR': 17.99, 'ZMK': 15830, 'GHS': 10.5, 'DEM': 1.99, 
              'USD': 1, 'CAD': 1.52, 'EUR': 1.14, 'Tola': 4, 'Temmy': 40}

mergedDict.pop("Temmy")
print(mergedDict)


# # Write a Python program to get the largest number from a list

# In[71]:


listEsden = [90, 28, 31, 23, 25, 59, 65]

def largestNum(listEsden):
    max = listEsden[0]
    for a in listEsden:
        if a > max:
            max = a 
    return max
print(largestNum(listEsden))


# In[ ]:




