#!/usr/bin/env python
# coding: utf-8

# In[4]:


#printing users name and age
try:
    name = input("type your name here: ")

    age = int(input("type your age here: "))
    
    gender = input("Your Gender: ")

except ValueError:
    print("invalid! type your name again!")
except TypeError:
    print("this should be a number. Try again")
    
if gender =='m' or gender =='male':
    print('Hello Mr. {}, you are {} years old.'.format(name, age))
elif gender =='f' or gender =='female':
    print('Hello Mrs. {}, you are {} years old.'.format(name,age))
else:
       print('Hello {}, you are {} years old.'.format(name,age))
    


# In[30]:


#print users date of birth
year = 2021
dob = year- int(age)
print('your year of birth is {}'.format(dob))


# In[31]:


#users age group
if (age <1):
    Group = "an Infant"
elif (age >=1) & (age <=11):
    Group = "a Child"
elif (age >=12) & (age <=17): 
    Group = "a Teens"
elif (age >=18) & (age <=64):
    Group = " an Adult"
else:
    Group = "Older Adult"
print('As you are {} years old, you are {}'.format(age,Group))


# In[32]:


#print users age a decade ago
decade=10
decade_year= year-decade
decade_ago =int(age)- decade
decade_ago,decade_year
print('As at {}, you were {} years old,'.format(decade_year,decade_ago))


# In[37]:


#print the age in the previous year and appending the users for the next 50 years to a new list
age_in_previous_year = int(input('What was your age last year? '))
previous_year = year-1
new_age = []
new_year = []

for i in range(10,60,10):
    new_a = age_in_previous_year + i
    new_age.append(new_a)
    #print(new_age)
    new_y = previous_year + i
    new_year.append(new_y)
   # print(new_year,new_age)

# the users age for the next 50 years
for i in range(len(new_age)):
    c= new_age[i]
    d= new_year[i]
    #print(c,d)
    print('In {} you will be {} years old'.format(d,c))

