
# This challenge creates a new parent class and then has
# two child classes inherit attributes from it

#create the parent class, in this case, Bike class

class Hamburger:
    patty = 'all beef patty'
    bun = True
    number_of_patties = 1
    vegi_add_on_1 = 'Lettuce'
    vegi_add_on_2 = 'Onion'
    condiment_1 = 'Ketchup'
    condiment_2 = 'Mustard'
    # method for putting items together
    def cook_method(self):
        cook_temp = 'medium rare'
        cook_type = 'gas grill'
        msg = 'You take the {} and put it on the {} until the patty is {}, then enjoy!'.format(self.patty, cook_type, cook_temp)
        return msg
        

class double_bacon_ched_burger(Hamburger):
    cheese = True
    cheese_type = 'Cheddar'
    meat_add_on_1 = 'Bacon'
    number_of_patties = 2
    # method for cooking with a change in how to cook the bacon
    def cook_method(self):
        meat_add_cook_temp = 'Crispy'
        meat_add_cook_type = 'Cast Iron'
        cook_temp = 'medium rare'
        cook_type = 'gas grill'
        msg = 'You take the {} and put it on the {} until the patty is {}, then you add the {} {} cooked in the {}, ENJOY!!'\
              .format(self.patty, cook_type, cook_temp, meat_add_cook_temp, self.meat_add_on_1, meat_add_cook_type)
        return msg
        


    

class mushroom_swiss(Hamburger):
    vegi_add_on_3 = 'Fried Mushrooms'
    cheese_type = 'Swiss Cheese'
    condiment_1 = 'None'
    # polymorphism for cooking addons with the inherited method
    def cook_method(self):
        vegi_add_cook_temp = 'Crispy'
        vegi_add_cook_type = 'Fryer'
        cook_temp = 'medium rare'
        cook_type = 'gas grill'
        msg = 'You take the {} and put it on the {} until the patty is {}, then you add the {} {} cooked in the {}, ENJOY!!'\
              .format(self.patty, cook_type, cook_temp, vegi_add_cook_temp, self.vegi_add_on_3, vegi_add_cook_type)
        return msg
        

    

if __name__ == '__main__':
    Dub_bac_chee = double_bacon_ched_burger()
    print(Dub_bac_chee.cook_method())
    mushroom_swiss = mushroom_swiss()
    print(mushroom_swiss.cook_method())




    
    
    
