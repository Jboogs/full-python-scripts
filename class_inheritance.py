
# This challenge creates a new parent class and then has
# two child classes inherit attributes from it

#create the parent class, in this case, Bike class

class Hamburger:
    patty = 'beef'
    bun = True
    number_of_patties = 1
    vegi_add_on_1 = 'Lettuce'
    vegi_add_on_2 = 'Onion'
    condiment_1 = 'Ketchup'
    condiment_2 = 'Mustard'

class double_bacon_ched_burger(Hamburger):
    cheese = True
    cheese_type = 'Cheddar'
    meat_add_on_1 = 'Bacon'
    number_of_patties = 2

class mushroom_swiss(Hamburger):
    vegi_add_on_3 = 'Grilled Mushrooms'
    cheese_type = 'Swiss Cheese'
    condiment_1 = 'None'




    
    
    
