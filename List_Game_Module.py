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



def coin_flip():
    NumOfStreaks = 0
    fliplst = []

    # Generate 10,000 random coin flips
    for _ in range(10000):
        if randint(0, 1) == 1:
            fliplst.append('H')  # Heads
        else:
            fliplst.append('T')  # Tails

    total_t_streaks = 0
    total_h_streaks = 0

    current_index = 0

    while current_index < len(fliplst):
        batch = fliplst[current_index: current_index + 100]  # Create a sublist of 100 values from fliplst

        t_streaks = 0
        h_streaks = 0

        # Count streaks in the current batch
        for i in range(len(batch) - 5): #Iterate through the batch
            if "T" * 6 in ''.join(batch[i:i + 6]):#count T
                t_streaks += 1
            if "H" * 6 in ''.join(batch[i:i + 6]):#count H
                h_streaks += 1

        total_t_streaks += t_streaks
        total_h_streaks += h_streaks

        # Move to the next batch
        current_index += 100

        print(f"Batch of 100 flips: {batch}")
        print(f"Number of Tails streaks in this batch: {t_streaks}" )
        print(f"Number of Heads streaks in this batch: {h_streaks}\n")

    # Calculate the total percentage of streaks for each separately
    percentage_t = (total_t_streaks / 10000) * 100
    percentage_h = (total_h_streaks / 10000) * 100

    print(f"Total number of Tails streaks: {total_t_streaks}")
    print(f"% of Tail streaks in the entire sample(size 10000): {percentage_t}")
  
    print(f"Total number of Heads streaks: {total_h_streaks}")
    print(f"% of Head streaks in the entire sample(size 10000): {percentage_h}")
