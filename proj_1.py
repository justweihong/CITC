 -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 15:23:54 2018

@author: Wei Hong
Spyder (Python 3.6)
"""

#importing the random function
import random 

#get string inputs from user, while loop makes sure user inputs integer ONLY
while True:
    length_str = input('Please enter the length for the list:')
    try:
        value = int(length_str)
        break
    except ValueError:
        print('That is not an integer! Please try again.')

while True:
    lower_bound_str = input('Please enter the lower bound for the range of integer values:')
    try:
        value = int(lower_bound_str)
        break
    except ValueError:
        print('That is not an integer! Please try again.')
  
while True:
    upper_bound_str = input('Please enter the upper bound for the range of integer values:')
    try:
        value = int(upper_bound_str)
        break
    except ValueError:
        print('That is not an integer! Please try again.')

#get integer values from the string inputs
length = int(length_str)
lower_bound = int(lower_bound_str)
upper_bound = int(upper_bound_str)

#generating the random integers on an empty list
generated_list = []
for x in range(length):
    generated_list.append(random.randint(lower_bound,upper_bound+1))

#printing the sequence and the details
print('Sequence:', generated_list)
print('Largest integer:', max(generated_list))
print('Smallest integer:', min(generated_list))
print('Sum:', sum(generated_list))
print('Average:', sum(generated_list)/length)
