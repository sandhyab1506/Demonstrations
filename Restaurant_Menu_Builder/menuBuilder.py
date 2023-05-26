#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Licence: MIT
#
#Author(s): Sandhya Buddharaju
#
#Program purpose:
#----------------
# 
# Task is to Display a Menu in the Format Specified below adhering the rules stated
#
#Program notes:
#--------------
#
# -----------------------------------------------------------------------------------
# Rules
# -----------------------------------------------------------------------------------
# 1) All the food categories and corresponding items are listed in food_categories
# 2) Display only the items the chef can prepare . They are listed in chef_dishes
# 3) Restaurant busy times can be determined by is_busy flag
# 4) At busy times the Menu have to be displayed in ascending order based on prep times listed in prep_times
#
# We assume the intial data be provided and stored in a list
#
#--------------------------------------------------------
"""
==== Example Restaurant ====
      ~ Menu ~

Starters
Dumplings, Peanuts or Salad

Mains
Bento, Sushi, Pasta or Rice

Desserts
Apples, Strawberries or Cheese
"""


# importing required functions
from Restaurant_Menu_Builder import menuFunctions

# Data Declarations
food_categories = {
    "starters": [
        "peanuts", "bread", "salad", "dumplings"
    ],
    "mains": [
        "steak", "bento", "chicken", "pizza", "sandwich", "taco", "sushi",
        "burger", "hotdog", "pasta", "wrap", "rice"
    ],
    "desserts": [
        "apples", "strawberries", "cheese", "icecream", "pie", "cake"
    ]
}

chef_dishes = [
    "strawberries", "dumplings", "pasta", "rice", "apples", "salad", "peanuts",
    "cheese", "bento", "sushi"
]

is_busy = True

prep_times = {
    "salad": 0.5,
    "pasta": 4,
    "pizza": 8,
    "burger": 6,
    "dumplings": 6,
    "strawberries": 10,
    "sushi": 7,
    "bento": 11,
}

# Printing the title
print("==== Example Restaurant ====      \n\t ~ Menu ~")

# Looping through the food_categories to extract required data
for category in food_categories:
    # printing the Food Category title
    print(f'{category.capitalize()}')

    # declaring the corresponding lists
    menu_items_list = []
    sorted_list_menu = []

    # extracting the items in each category
    for category_item in food_categories[category]:
        # extracting only the items that the chef can prepare
        if category_item in chef_dishes:
            menu_items_list.append(category_item)

    # building the menu as per the busy schedule
    if is_busy:
        # if the restaurant is busy the menu is sorted as per prep times supplied
        sorted_list_menu = menuFunctions.menu_to_sort(menu_items_list, prep_times)
    else:
        sorted_list_menu = menu_items_list

    # displaying the menu
    menuFunctions.menu_list_to_print(sorted_list_menu)
