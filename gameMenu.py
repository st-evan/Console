from sys import exit
from itertools import islice

menu = { #A dict{dict{}} featuring multiple games in dictionaries of their game category
    'GameCat1': {
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
        query = input('\nShall we begin? ')
        if query == '' or not query[0].lower() in ['y','n']: #Checks user input
            print('Error: Yes or No?')
        elif query[0].lower() in ['y']:
            with open('Welcome Message.txt') as lines: #Reads welcome message from a file
                for line in islice(lines, 7):
                    print(line, end="")
            self.show_categories() #Calls show_category after welcome message

    def show_categories(self):
        print('\n\nAvailable game categories are:') 
        for category in menu.keys():
            print(category) #.keys() calls main dict key value
        Cat_obj = input('\nPlease choose or create a category: ')
        self.show_Games(Cat_obj)

    def show_Games(self, category):
        if category in menu:
            game = menu[category] #what?
            for game, description in game.items():
                print(f'{game} : {description}')
        else:
            query = input('\nYour chosen category is not defined. Would you like to define your own game category?\n')
            if query == '' or not query[0].lower() in ['y','n']:
                    print('Dont be silly! Yes or No?')
            elif query[0].lower() in ['y']:
                game = input('\nPlease enter a game name: ')
                description = input('\nplease enter a description of your game: ')
                self.new_Category(category, game, description)
            else:
                print('GoodBye')
                exit()

    def new_Category(self, category, game, description):
        menu[category] = {}
        menu[category][game] = description
        print(f'Added "{game}" to the "{category}" with description: "{description}"')
       # query = input('\nWould you like to exit?')





menu_display = display_menu() #instance of the class
#print('Game categories are')
#menu_display.show_categories() #display default game categories

#print(f'\nGames in {MyCatOBJ} category are:')