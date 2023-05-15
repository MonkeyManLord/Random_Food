import requests, json
#from time import sleep
#https://www.themealdb.com/api.php
#https://www.themealdb.com/api/json/v1/1/random.php

#// Let the people only click the button once
## Must re-access api to recieve a new meal

#uses requests to get meal from api, calls other methods
def get_food():
    try:
        response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
        data = response.json()
        str_meal = data['meals'][0]['strMeal']
        answer = input('\n' + str_meal + '\nLearn more? ')
        if 'y' in answer.lower():
            #// THIS LINE IS READING OUT THE INGREDIENTS
            print_ingredients(get_ingredients(data))
        else:
            get_food()
    except requests.exceptions.RequestException as e:
        print('You might not have a Wifi connection... Error:', e)

#returns ingredients in: [amount][measurement] - [ingredient]
def get_ingredients(data):
    ingredients = []
    for i in range(1, 21):
        ingredient_key = 'strIngredient' + str(i)
        measure_key = 'strMeasure' + str(i)
        ingredient = data['meals'][0][ingredient_key]
        measure = data['meals'][0][measure_key]
        if ingredient:
            if measure: 
                ingredients.append(f"{measure} - {ingredient}")
            else:
                ingredients.append(ingredient)
    return ingredients

#printing for test - will delete later
def print_ingredients(ingredients):
    if ingredients:
        print("Ingredients:")
        for ingredient in ingredients:
            print(ingredient)
    else:
        print("No ingredients found.")

#! Get Functions START-------------------------------------------------------------------

def get_YT(data):
    #in new tab open the ytvid when clicked
    link = data['meals'][0][strYoutube]
    return link

def get_picture(data):
    picture = data['meals'][0][strMealThumb]
    return picture
    
def get_source(data):
    source = data['meals'][0][strSource]
    
def get_mealType(data):
    mealType = data['meals'][0][strTags]
    return mealType

def get_info(data):
    info = data['meals'][0][strArea] 
    info2 = data['meals'][0][strCategory]
    if  info2:
        info = info + ' - ' + info2
    return info  
    
def how_make(data):
    #tells how to make it
    instructions = data['meals'][0][strInstructions]
    return instructions

#! Get Functions END-------------------------------------------------------------------


womp = input("Can't decide what to eat? ")
if "y" in womp.lower():
    get_food()
else:
    print("Congrats!")