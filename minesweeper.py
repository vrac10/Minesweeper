import random as r
import numpy as np

coordinates = [(x,y) for x in range(8) for y in range(8)]
entries = []
a = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
print(a)
coord_input = input("Enter the coordinates of the first click ").split(",")
coord = (int(coord_input[0]),int(coord_input[1]))
coordinates.remove(coord)
a[coord[0]][coord[1]] = -2
print(a)
def getAdjacent(arr,i,j):
    n = len(arr)
    m = len(arr[0])
 
    v = []
    for dx in range (-1 if (i > 0) else 0 , 2 if (i < n) else 1):
        for dy in range( -1 if (j > 0) else 0,2 if (j < m) else 1):
            if (dx is not 0 or dy is not 0):
                v.append(arr[i + dx][j + dy])
    return v

def add_mines(coords, matrix):
    mines = r.choices(coords,k=10)
    for i,j in mines:
        matrix[i][j] = -1
    return mines
    
mines = add_mines(coordinates,a)
print(mines)

while(1):
    coord_input = input("Enter the coordinates of the click ").split(",")
    coord = (int(coord_input[0]),int(coord_input[1]))
    if coord not in mines: 
        adjacent = getAdjacent(a,coord[0],coord[1]).count(-1)
        if adjacent == 0:
            a[coord[0]][coord[1]] = -2
        else:
            a[coord[0]][coord[1]] = adjacent
        print(a)
    else:
        break

def random_openings(inputs, )


print(a)
