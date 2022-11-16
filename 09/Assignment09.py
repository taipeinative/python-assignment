# -*- coding: utf-8 -*-
"""Assignment09.ipynb

1. This Colab is designed for the course "[REDACTED]" instructed by [REDACTED].

2. First, copy this Colab notebook to your Drive. Then, read the instruction of this assignment. 

3. Rename the copied Colab page to [REDACTED]. For example, [REDACTED]

4. When you complete your assignment, you need to:

  a. First, **download** your Colab notebook as a IPYNB file

  b. Next, **upload** the IPYNB file to the specific drive folder [REDACTED] before [REDACTED]

  c. Then, **submit** the link of your uploaded file to [REDACTED]. 
  
  The link of **uploaded** IPYNB file can be found by clicking **Share>Get Link** on the top right on the Colab page you upload.
  
Note that you can re-submit your assigment by replacing the old one.

## Personal Information
Please fill in your details below.

Name: [REDACTED]

Student ID: [REDACTED]

Department/Program: [REDACTED]
"""

# Load packages
import pandas as pd

"""## Pandas: Revisited of Diet record

Consider a variant of diet record from assignment 7 as follows: 
"""

# [DO NOT MODIFY] Define date and diet records as two lists
date_list = ['10/26', '10/27', '10/28', '10/29', '10/30']
record_list = [[{'meal_type': 'Breakfast', 'food_type': 'Salad', 'order_place': 'Vendor'},
                {'meal_type': 'Lunch', 'food_type': 'Burger', 'order_place': 'Vendor'},
                {'meal_type': 'Dinner', 'food_type': 'Soup', 'order_place': 'Vendor'}],
               [{'meal_type': 'Breakfast', 'food_type': 'Fried rice', 'order_place': 'Resturant'},
                {'meal_type': 'Lunch', 'food_type': 'Burger', 'order_place': 'Vendor'}],
               [{'meal_type': 'Breakfast', 'food_type': 'Pizza', 'order_place': 'Cooking at home'},
                {'meal_type': 'Lunch', 'food_type': 'Salad', 'order_place': 'Cooking at home'},
                {'meal_type': 'Dinner', 'food_type': 'Pizza', 'order_place': 'Vendor'}],
               [{'meal_type': 'Breakfast', 'food_type': 'Noodle', 'order_place': 'Dining car'},
                {'meal_type': 'Lunch', 'food_type': 'Fried rice', 'order_place': 'Vendor'},
                {'meal_type': 'Dinner', 'food_type': 'Noodle', 'order_place': 'Vendor'}],
               [{'meal_type': 'Lunch', 'food_type': 'Pizza', 'order_place': 'Resturant'},
                {'meal_type': 'Dinner', 'food_type': 'Burger', 'order_place': 'Cooking at home'}]]

# [DO NOT MODIFY] Assemble date and diet records into a dict
data = {'Date': date_list,
        'Records': record_list}
data

"""``data`` is a dict with two keys ``Date`` and ``'Records'`` which represents a dietary recored of all meals from 10/26 to 10/31. 

The value of the key ``'Records'`` is ``date_list``, a list of strings for each date 10/26 to 10/31. 

The value of the key ``'Records'`` is ``record_list``, a very nested structure, more precisely, ``record_list`` is a list of 5 lists of 3 dicts.

If we don't preprocess ```record_list```, then we may get an unexpected data frame as follows:
"""

# [DO NOT MODIFY] Display of the data frame from the diet record directly
df = pd.DataFrame(data)
df

"""In this exercise, you could try different approaches by using 
* nested structure of dicts, 
* NumPy arrays, or 
* Pandas DataFrames.

### 1. Single Meal as a Single Data

Now, we would like to expand each entry in Records column into an individual row as follows:

If the following figure cannot be loaded properly, please click the [link](https://drive.google.com/uc?export=view&id=1ERBYkOrtHdltC5vau9NAD4WZ9-bu-lYC) to check the figure. 

<img src='https://drive.google.com/uc?export=view&id=1ERBYkOrtHdltC5vau9NAD4WZ9-bu-lYC' width="640" height="360">
"""

# Write a program to create the data frame on the right in above figure, and name it df_v

# Pre-defined arrays: They are intended to store the value we are going to 
# search, using Depth-First-Search (DFS).
#
# We already knew that the data structure of 'record_list' looks like how 
# following diagram illustrates:
#
#                            record_list                        
#   ┌───────────────────────────────────────────────────────────┐
#   │     (10/26)        (10/27)                    (10/30)     │
#   │ ┌─────────────┐┌─────────────┐            ┌─────────────┐ │
#   │ │ (Breakfast) ││ (Breakfast) │            │   (Lunch)   │ │
#   │ │ ┌─────────┐ ││ ┌─────────┐ │            │ ┌─────────┐ │ │
#   │ │ │meal_type│ ││ │meal_type│ │  Omission  │ │meal_type│ │ │
#   │ │ │food_type│ ││ │food_type│ │   ......   │ │food_type│ │ │
#   │ │ │order_...│ ││ │order_...│ │            │ │order_...│ │ │
#   │ │ └─────────┘ ││ └─────────┘ │            │ └─────────┘ │ │
#   │ │   (Lunch)   ││   (Lunch)   │            │   (Dinner)  │ │
#   │ │ ┌─────────┐ ││ ┌─────────┐ │            │ ┌─────────┐ │ │
#   │ │ │meal_type│ ││ │meal_type│ │            │ │meal_type│ │ │
#   │ │ │food_type│ ││ │food_type│ │            │ │food_type│ │ │
#   │ │ │order_...│ ││ │order_...│ │            │ │order_...│ │ │
#   │ │ └─────────┘ ││ └─────────┘ │            │ └─────────┘ │ │
#   │ │   (Dinner)  │└─────────────┘            └─────────────┘ │
#   │ │ ┌─────────┐ │                                           │
#   │ │ │meal_type│ │                                           │
#   │ │ │food_type│ │                                           │
#   │ │ │order_...│ │                                           │
#   │ │ └─────────┘ │                                           │
#   │ └─────────────┘                                           │
#   └───────────────────────────────────────────────────────────┘
#
# In order to access to these values, we have to look into 3 levels, for example,
# if I want to access to the food_type of dinner on 10/30, I have to query by 
# the statement record_list[-1][-1]['meal_type'].

datesList = []
mealList = []
foodList = []
placeList = [] 

for i in range(len(date_list)): # Look through first level (dates)

  for j in range(len(record_list[i])): # Look through second level (number of meals)

    # Following are looking through third level (details of each meal)
    datesList.append(date_list[i])
    mealList.append(record_list[i][j]['meal_type'])
    foodList.append(record_list[i][j]['food_type'])
    placeList.append(record_list[i][j]['order_place'])

# Combined them together into a new dictionary
sortedData = {'Date': datesList, 'Meal': mealList, 'Food': foodList, 'Order Place': placeList}
# Convert into data frame
df_v = pd.DataFrame(sortedData)

# [DO NOT MODIFY] Expected Data Frame
df_v

"""### 2. Daily Record as a Single Data

Here, we would like to represent each meal information as a new column for the same date as follows:

If the following figure cannot be loaded properly, please click the [link](https://drive.google.com/uc?export=view&id=1hOyK4RzaMeolb9wFg9DctKCs3_edbu-c) to check the figure. 

<img src='https://drive.google.com/uc?export=view&id=1hOyK4RzaMeolb9wFg9DctKCs3_edbu-c' width="640" height="360">
"""

# Write a program to create the data frame on the right in above figure, and name it df_h
# We will continue using the same technique which solved first problem.
# First, prepare arrays:        

datesVList = []
breakfastVList = []
lunchVList = []
dinnerVList = []

for k in range(len(date_list)): # Look through first level (dates)

  for l in range(len(record_list[k])): # Look through second level (meals)

    item = record_list[k][l] # To save time and tidy up

    # Look through third level, add value into coresponding list if condition is true

    if item.get('meal_type') == 'Breakfast': 
      breakfastVList.append(item.get('food_type')) 

    if item.get('meal_type') == 'Lunch':
      lunchVList.append(item.get('food_type'))

    if item.get('meal_type') == 'Dinner':
      dinnerVList.append(item.get('food_type'))

  datesVList.append(date_list[k])

  # We already knew that we have 3 meals (breakfast, lunch and dinner) a day, so
  # for each loop, we should have appended 1 element to following lists, unless
  # something is missing. By checking the element quantities, we could find what
  # is missing and append 'AIR' back. 

  breakfastVList.append('AIR') if len(breakfastVList) != k + 1 else None
  lunchVList.append('AIR') if len(lunchVList) != k + 1 else None
  dinnerVList.append('AIR') if len(dinnerVList) != k + 1 else None

# Combined them together into a new dictionary
reallySortedData = {'Date': datesVList, 'Breakfast': breakfastVList, 'Lunch': lunchVList, 'Dinner': dinnerVList}
# Convert into data frame
df_h = pd.DataFrame(reallySortedData)

# [DO NOT MODIFY] Expected Data Frame
df_h

"""# (Bonus) Design your own Python exercise 

In this part, you could got additional 1 point with your creativity.

Consider a scenario that you are a Python instructor. Based on recent course materials such as NumPy and Pandas, please design a Python exercise for your students (that is, other classmates). 

Note that you have to describe proposed exercise in detail such as the expected result, however, the solution manual of this exercises is optional, but I encourage you to give your own solution if possible. 
"""

