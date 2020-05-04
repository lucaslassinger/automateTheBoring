#Conways Game of Life
import random, time, copy

#Global Constants
WIDTH = 6
HEIGHT = 6

#List for Cells
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) ==0:
            column.append('#') #Add live cells
        else:
            column.append(' ') #add dead cell
    nextCells.append(column) #nextCells is a list of column lists.
while True: #Main loop
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    #Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end=' ') #print # or space
        print() #print new line at end of row

    #Calculate next step cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #get neighboring coordinates
            #'% width' ensures leftCoord is always between 0 and WIDTH-1
            leftCoord = (x-1) %WIDTH
            rightCoord = (x+1) %WIDTH
            aboveCoord = (y-1) %HEIGHT
            belowCoord = (y+1) %HEIGHT

            #Count number of living neigbors
            numNeighbors = 0
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

            #set cell based on rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #living with 2 or 3 beside survive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '

        time.sleep(1)
