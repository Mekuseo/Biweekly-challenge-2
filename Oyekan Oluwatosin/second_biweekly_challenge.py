#!/usr/bin/env python
# coding: utf-8

# # Bi-weekly Challenge 

# ### Write a python program that prompts for inputs from the user. The inputs should be the user's name and the age.

# In[4]:


# declare user's name and age input

user_name= str(input())
age = int(input())


# In[6]:


# Print the user’s name and age


# concatinate the strings and input
print('Hello ' + user_name + ',' + ' you are ' + str(age) + ' years old')


# In[7]:


# Calculate the user’s DOB using the age and print to screen

# creating the user_DOB function
year = 2020
user_DOB = year - age

# printing the output
print('Your year of birth is ' + str(user_DOB ))


# In[8]:


# State which age group the user belongs to

# Legend
# Infants: <1
# Children: 1-11 years
# Teens: 12-17 
# Adults: 18-64
# Older Adults: 65+


if age < 1:
    print('As you are ' + str(age) + ' years old, you are an infant')
elif (age >=1) & (age <=11):
    print('As you are ' + str(age) + ' years old, you are a children')
elif (age >=12) & (age <=17):
    print('As you are ' + str(age) + ' years old, you are a teen')
elif (age >=18) & (age <=64):
    print('As you are ' + str(age) + ' years old, you are an adult')
else:
    print('As you are ' + str(age) + ' years old, you are a older adult')


# In[9]:


# What was the user’s age a decade ago?

decade_age = age - 10
decade_age


# In[10]:


# For the next 50 years, print what the user’s age will be after every decade (NB: The current year is 2020 :))

new_age = []  # declaring a list for the new age
new_year = [] # declaring a list for the new year

for x in range(10,60,10): 
    age_new = age + x
    new_age.append(age_new)
    year_new = x + year
    new_year.append(year_new)
    
for x in range(len(new_age)):
  new_a = new_age[x]
  new_y = new_year[x]

  print(" In " + str(new_y) + " you'll be " + str(new_a) + "y.o")




# ## Writing codes to function

# In[ ]:


def age_func(input):
    try:
        user_name= str(input())
        age = int(input())
        print('Hello ' + user_name + ',' + ' you are ' + str(age) + ' years old')
    except ValueError:
        print('Oops that was not a valid number')
    except TypeError:
        print('Argument must be a number')
    try:
        year = 2020
        user_DOB = year - age
        print('Your year of birth is ' + str(user_DOB ))
    except ValueError:
        print('Oops that was not a valid number')
    except TypeError:
        print('Argument must be a number')
    
    if age < 1:
        print('As you are ' + str(age) + ' years old, you are an infant')
    elif (age >=1) & (age <=11):
        print('As you are ' + str(age) + ' years old, you are a children')
    elif (age >=12) & (age <=17):
        print('As you are ' + str(age) + ' years old, you are a teen')
    elif (age >=18) & (age <=64):
        print('As you are ' + str(age) + ' years old, you are an adult')
    else:
        print('As you are ' + str(age) + ' years old, you are a older adult')
        
        
    decade_age = age - 10
    print('I was ' + str(decade_age) + 'years old a decade ago')
    
    
    new_age = []
    new_year = [] 
    

    for x in range(10,60,10): 
        age_new = age + x
        new_age.append(age_new)
        year_new = x + year
        new_year.append(year_new)
    
    for x in range(len(new_age)):
          new_a = new_age[x]
          new_y = new_year[x]

          print(" In " + str(new_y) + " i'll be " + str(new_a) + "y.o")


# In[15]:


age_func(input)

