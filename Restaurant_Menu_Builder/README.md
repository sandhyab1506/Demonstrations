# Task is to Display a Menu in the Format Specified below adhering the rules stated

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
# -----------------------------------------------------------------------------------
# Rules
# -----------------------------------------------------------------------------------
# 1) All the food categories and corresponding items are listed in food_categories
# 2) Display only the items the chef can prepare . They are listed in chef_dishes
# 3) Restaurant busy times can be determined by is_busy flag
# 4) At busy times the Menu have to be displayed in ascending order based on prep times listed in prep_times

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
