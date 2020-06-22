#
#
#   Python Version: 3.8
#
#   Author: Justin Perry
#
#   The intention of this software is to make a game and learn
#   how to connect variables and functions together with return
#   methods and parameters/arguments
#
#   This is called the nice or mean game!
#   Have fun!
#

# This is the function that begins the game being called through the dunder
# then calling the function below, get_number
def start(nice=0, mean=0, name=""): # if this is a play again, name will be stored as before
    #get the users name and pass it into the describe game function
    name = describe_game(name)
    # all three variable are calling the nice_mean() function as passing that in
    nice, mean, name = nice_mean(nice, mean, name)

# When the describe_game() function is called passing in name parameters
def describe_game(name):
    '''
    Check to see if this is a new game.
    If new game, get the users name.
    If not, thank the player for playing
    again and continue with playing
    '''
    #if we do not already have the user info, then they are a new player
    #if their name is not blank at this point, they are not a new player and thanks for playing again is printed
    if name != "":
        print('\nThanks for playing again, {}!'.format(name))
    else: #this else statement will have the user enter their info if they are a new player
        stop = True
        while stop:# this also means stop == True:
            if name == "":
                name = input('What is your name? \n>>>').capitalize()
                if name != "": # after new player enters his name, the game descrip shows up
                    print('\nWelcome to the game {}'.format(name))
                    print('\nIn this game you will be greeted\nby several different people.\nYou can choose to be nice or mean!')
                    print('\nBut in the end, your fate\nwill be decided by your actions!')
                    # change stop to False so they can now play again with out entering their name as name is
                    # now saved in the variable
                    stop = False
    return name

# this is the nice_mean(nice, mean, name) function being called next in the game after
# user enters their name (if new) or continues to play a new game.

def nice_mean(nice, mean, name): # default values for this are passed in for nice, mean but the name is passed in from describe_game()
    stop = True # this boolean will continue or stop the flow of the game
    while stop == True:
        show_score(nice, mean, name) # while stop is true, call show_score() function with the parameters listed next
        #this is the user input, giving them choices of N or M, which are then set to lower case and used in the statement below
        # input statements end with three chevrons to indicate an input is wanted
        pick = input('\nA stranger approaches you looking to converse.\nWill you be nice or mean??? (N/M) \n>>>').lower() 
        if pick == 'n':
            print('\nThe strange person walks away smiling, strange....')
            # add plus one to what the nice variable is already (if new, 0 + 1)
            nice = (nice + 1)
            # change stop bool to false to stop the code from moving forward and throwing an error
            stop = False
        if pick == 'm':
            print('\nThe stranger stares at you like you insulted his great grandmother, he storms off...')
            mean = (mean + 1)
            stop = False
    score(nice, mean, name) # pass the three variables to the score() function


# this function will show the score on the screen with arguments passed from nice_mean() function

def show_score(nice, mean, name):
    print('\n{}, your current score is: \nNice: {} \nMean: {}'.format(name, nice, mean))

# this function keeps track of score and how much to be a nice guy or an asshole
def score(nice, mean, name):
    # the three parameters are passed into the function
    if nice > 2:
        win(nice, mean, name) #if the win condition is valid, call the win function
    if mean > 2:
        lose(nice, mean, name) # if losing condition is valid, call the lose function
    else:
        nice_mean(nice, mean, name) # if neither are true, circle back to the nice_mean() function

# win() block of code
def win(nice, mean, name):
    print('\nNice job {}, you aren\'t that big of an asshole! \nEvery one seems to love you too!'.format(name))
    # this will call the function to see if you want to play again
    again(nice, mean, name)

# lose() block of code
def lose(nice, mean, name):
    print('\nNice job {}, you are a big asshole! \nEvery one seems to avoid you now!'.format(name))
    # this will call the function to see if you want to play again
    again(nice, mean, name)


# this again() function will ask if you want to play again and receive user input
def again(nice, mean, name):
    stop = True # this will stop the code from running further once a choice is made
    while stop == True:
        choice = input('Do you want to play again? (Y/N) \n>>>').lower()
        if choice == 'y':
            stop = False #stops the code after this is chosen
            reset(nice, mean, name) # calls reset() to resart the game
        if choice == 'n':
            print('\nSo sad, sorry to see ya go, boss!')
            stop = False # stops code after this is chosen
            quit() # quits the function, built in python function
        else:
            print('\nEnter ( Y ) for YES or ( N ) for NO \n>>>') # starts the while loop over because stop is not changed to false

# this will reset the score of the game if user chooses to play again
def reset(nice, mean, name):
# reset the nice and mean score back to 0 for a new game
    nice = 0 
    mean = 0
    # do not reset name as the user is playing again
    start(nice, mean, name) #this is the original starting function
            












if __name__ == "__main__":
    start()
