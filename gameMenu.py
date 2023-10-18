"""
Trying to construct an interactive menu
loop to recieve Yes/No input

while True:
    query = input('\nshall we begin?\n ') #\n supposed to receive input in nextline
    if query == '' or not query[0].lower() in ['y','n']: #Will not accept answers not starting with 'y' or 'n'
        print('HaHa Dont do that! Yes or No?')
    else:
        break #Break loop
"""
menu = { #Dictionary of GameMenu: Here we have a dict of dict featuring different games in dictionaries of their game category
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

#Class so this damn thing can be imported tfffff
class main_menu(): #Game menu class
    def show_categories(self): #Show game category
        for category in menu.keys():
            print(category)


    def show_Games(self, category): #show games
        if category in menu:
            game = menu[category]
            for game, description in game.items():
                print(f'{game}:{description}')
        else:
            print(f'Category {category} does not exist')
            #should pass an do yu want to try again or some typer continuation clause

    def new_Category(self, category, game, description):
        if category not in menu:
            while True:
                query = input('\nYour chosen category is not defined. Would you like to define your own game category?\n')
                if query == '' or not query[0].lower() in ['y','n']:
                    print('Dont be silly! Yes or No?')
                elif query[0].lower() in ['y']:
                    menu[category] = {}
                    menu[category][game] = description
                    print(f'Added "{game}" to the "{category}" with description: "{description}"')
                else:
                    break




menu_display = main_menu() #instance of the class
print('Game categories are')
menu_display.show_categories() #display default game categories

MyCatOBJ = 'GameCat4'
print(f'\nGames in {MyCatOBJ} category are:')
menu_display.show_Games(MyCatOBJ)
