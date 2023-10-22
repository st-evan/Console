from sys import exit
from itertools import islice
from time import sleep

menu = { #A dict{dict{}} featuring multiple games in dictionaries of their game category
    'Lists': {
        'Game1':'Description of G1',
        'Game2':'Description of G2',
        'Game3':'Description of G3'
    },
    'GameCat2': {
        'Game1.1':'Description of G1',
        'Game2.1':'Description of G2',
        'Game3.1':'Description of G3'
    },
    'GameCat3': {
        'Game1.2':'Description of G1',
        'Game2.2':'Description of G2',
        'Game3.2':'Description of G3'
    }
}

#A class so this menu display architecture can be imported and reused
class display_menu(): #Game menu class
    def __init__(self):
        #user_name = input("Hello, what is your name? ")
        #print("Do hold on, Mr", user_name)
        #for char in "Loading...":
            #print(char,end="",flush=True)
            #sleep(0.5)
        
      
        #Condition to check how many times user entered wrong input
        wrong_input_counter = 0
        while wrong_input_counter < 3:
            query = input('\nShall we begin? ')
            if query == '' or not query[0].lower() in ['y','n']:#Checks user input is empty string or is not yes or no
                wrong_input_counter +=1
                if wrong_input_counter == 3: #When wrong input has been entered thrice
                    exit_program = input("\nInvalid!! Do you want to exit?(y/n): ")
                    if exit_program.lower() == "y":
                        print("Unserious priq")
                        exit()
                    elif exit_program[0].lower() in ['n']:
                            wrong_input_counter = 0
                    elif exit_program == '' or not query[0].lower() in ['y','n']:
                        exit()                       
                print('Error: Yes or No?')
            
            #Reads welcome message from a file if true and Calls show_category() after welcome message
            elif query[0].lower() in ['y']:
                with open('Welcome Message.txt') as lines:
                    for line in islice(lines, 7):
                        print(line, end="")
                        #sleep(0.5)
                #sleep(0.5)
                self.show_categories()
            
            elif query[0].lower() in ['n']:
                print("Well fok off then")
                exit()
            
    def show_categories(self):
        print('\n\nAvailable game categories are:')
        for category in menu.keys():
            print(category) #.keys() calls main dict key value
            sleep(0.5)
        choice = input('\nPlease choose or create a category: ')
        self.show_Games(choice)

    def show_Games(self, category):
        categoryLC = category.lower()
        if categoryLC in [key.lower() for key in menu]: #creates a list comprehension of keys in menu_dict
            categoryVar = next(key for key in menu if key.lower() == categoryLC)#A generator expresson inside a next() func
            gameVar = menu[categoryVar] #what?
            for game, description in gameVar.items():
                print(f'{game} : {description}')
            self.load_game(game)##################
        else:
            query = input('\nYour chosen category is not defined. Would you like to define your own game category?\n')
            if query == '' or not query[0].lower() in ['y','n']:
                    print('Dont be silly! Yes or No?')
            elif query[0].lower() in ['y']:
                game = input('\nPlease enter a game name: ')
                description = input('\nplease enter a description of your game: ')
                self.new_Category(category, game, description)#Allows user to add a new game and category
            else:
                print('GoodBye')
                exit()

    def new_Category(self, category, game, description):
        menu[category] = {}
        menu[category][game] = description
        print(f'Added "{game}" to the "{category}" with description: "{description}"\nAdd game feature coming soon!')
       # query = input('\nWould you like to exit?')

    def load_game(self,game):
        print(game)




menu_display = display_menu() #instance of the class
#print('Game categories are')
#menu_display.show_categories() #display default game categories

#print(f'\nGames in {MyCatOBJ} category are:')