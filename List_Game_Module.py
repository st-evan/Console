from random import randint
from time import sleep
from copy import deepcopy

def fortune_teller():
    Fortune = [
        'It is certain',
        'It is decidedly so',
        'Yes, definitely',
        'Very hazy, my child. Ask again',
        'Concentrate and ask again',
        'My reply is no',
        'The outlook is not so good',
        'Very very doubtful']

    print(Fortune[randint(0,len(Fortune)-1)])

def game_of_life():
    WIDTH = 20
    HEIGHT = 10

    #create a list of list for the cells
    nextCells = [] 
    for x in range(WIDTH):
        column = [] #Create a column list
        for y in range(HEIGHT):
            if randint(0,1) == 0:
                column.append('#') #Add living cell
            else:
                column.append(' ') #Add dead cel
        
        nextCells.append(column)#A list of column lists

    while True: #Main program loop
        print('\n') #Seperate each step with a new line
        currentCells = deepcopy(nextCells) #

        #print currentCells on the screen
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(currentCells[x][y], end='')
                print()

        #Calculate the next step's cell based on current step's cell
        for x in range(WIDTH):
            for y in range(HEIGHT):
                #get neighboring coordinates
                leftCoord = (x - 1) % WIDTH
                rightCoord = (x + 1) % WIDTH
                aboveCoord = (y - 1) % HEIGHT
                belowCoord = (y + 1) % HEIGHT
                
                numNeighbors = 0 #Num of living neighbors
                if currentCells[leftCoord][aboveCoord] == '#':
                    numNeighbors += 1
                if currentCells[x][aboveCoord] == '#':
                    numNeighbors += 1
                if currentCells[rightCoord][aboveCoord] == '#':
                    numNeighbors += 1
                if currentCells[leftCoord][y] == '#':
                    numNeighbors += 1
                if currentCells[rightCoord][y] == '#':
                    numNeighbors += 1
                if currentCells[leftCoord][belowCoord] == '#':
                    numNeighbors += 1
                if currentCells[x][belowCoord] == '#':
                    numNeighbors += 1
                if currentCells[rightCoord][belowCoord] == '#':
                    numNeighbors += 1

                if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                    nextCells[x][y] = '#'
                elif currentCells[x][y] == ' ' and numNeighbors == 3:
                    nextCells[x][y] = '#'
                else:
                    nextCells[x][y] = ' '

        sleep(1)

game_of_life()
