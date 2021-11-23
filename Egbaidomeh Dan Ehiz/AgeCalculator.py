#!/usr/bin/env python
# coding: utf-8

# In[27]:



# write a python program that prompts for inputs from the user. The inputs should be the user's name and the age.
# Print the user’s name and age
# Calculate the user’s DOB using the age and print to screen
# State which age group the user belongs to  How are the different age groups defined? – Conduent Healthy Communities Institute
# What was the user’s age a decade ago? (print to screen)
# For the next 50 years, print what the user’s age will be after every decade (NB: The current year is 2020 :))
# 
# SAMPLE OUTPUT:
# 
# Hello John Doe, you are 3 years old  \
# Your year of birth is 2051  \
# As you are 3 years old, you are an adult \
# In 2046 you were -7 years old  \
# In 2064 you’ll be 13y.o \
# In 2074 you’ll be 23y.o \
# .
# .
# In 2104 you’ll be 53y.o
# 

# In[34]:


# import date from date module
from datetime import date
y = date.today().year
m = date.today().month
d = date.today().day
print (date.today())

# enter input message prompting user for inputs
name = str(input('Enter your name'))
year = int(input('Enter your birth year'))
month = int(input('Enter your birth month'))
day = int(input('Enter your birth day'))


# Define year of birth
age_year = y - year

if (year > 2021) or (year < 1900):
    print('Oops, your input seems wrong. Pls enter a correct input')
elif (month > 12) or (month < 1):
    print('Oops, your input seems wrong. Pls enter a correct input'),
elif (day > 31) or (day < 1):
    print('Oops, your input seems wrong. Pls enter a correct input'),


# Calculate the birth year, month, and day of the user
if day> d and month >= m:
    dd = (d + 30) - day
    mm = ((m - 1) + 12) - month
    yy = (y - 1) - year
    print ('Hello {}, you are {} years, {} months and {} days old '. format(name,yy, mm, dd)
                              )
              

elif day> d and month < m:
    dd = (d + 30) - day
    mm = m - month
    yy = y - year
    print ('Hello {}, you are {} years, {} months and {} days old '. format(name,yy, mm, dd)
                          )


elif day< d and month > m:
    dd = d - day
    mm = (m + 12) - month
    yy = (y - 1) - year
    print ('Hello {}, you are {} years, {} months and {} days old '. format(name,yy, mm, dd)
                          )

elif day< d and month < m:
    dd = (d - day)
    mm = m - month
    yy = y - year
    print ('Hello {}, you are {} years, {} months and {} days old '. format(name,yy, mm, dd)
                          )
 
    
# Age classification
try:
    if (age_year < 2):
        cat = ' an infant'
    elif (age_year > 2) & (age_year <12):
        cat = ' a child'
    elif (age_year > 11) & ( age_year< 18):
        cat = ' a teenager'
    elif (age_year > 17) & (age_year < 65):
        cat = ' an adult'
    elif (age_year > 65) & (age_year < 120):
        cat = ' an older adult' 
    print('As you are {} years old, you are {}'.format (age_year, cat))
except:
    print('Oops, your input seems wrong')


newAge = []
newYear = []
for x in range(10,60, 10):
  newAGE = age_year + x
  newAge.append(newAGE)
  newYEAR = y + x
  newYear.append(newYEAR)

for x in range(len(newAge)):
  a = newAge[x]
  b = newYear[x]
  print('In {}, you would be {} year of age'.format(b,a))

