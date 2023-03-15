from tkinter import *
import time, random, copy
from Shapes import *

#################
width = 40
#################

print("1. Create a grid using newGrid(width,height)")
print("2. Insert blocks using insert(block,x position, y position)")
print("3. Reprint grid printGrid()")
print("4. Fill in random blocks with find()")
print("5. Or use wave function collapse to insert using fill(x position,y position)")
print("6. Find the rest of the blocks with finish()")
print("\n")
print("- run() will create and fill a 20x20 grid with random blocks")
print("- displayBlocks() will create a grid showing you all the available blocks")

blocks = {
    "zero":(0,0,0,0),
    "one":(0,0,0,1),
    "two":(0,0,1,0),
    "three":(0,0,1,1),
    "four":(0,1,0,0),
    "five":(0,1,0,1),
    "six":(0,1,1,0),
    "seven":(0,1,1,1),
    "eight":(1,0,0,0),
    "nine":(1,0,0,1),
    "ten":(1,0,1,0),
    "eleven":(1,0,1,1),
    "twelve":(1,1,0,0),
    "thirteen":(1,1,0,1),
    "fourteen":(1,1,1,0),
    "fifteen":(1,1,1,1),
}

def toCardinal(x):
    if x in blocks:
        x = blocks[x]
    n,e,s,w = x
    return n,e,s,w

def Compare(new,initial): #returns Array
    n,e,s,w = toCardinal(new)
    n2,e2,s2,w2 = toCardinal(initial)
    validDirection = []
    if(n == s2):
        validDirection.append("south")
    if(s == n2):
        validDirection.append("north")
    if(e == w2):
        validDirection.append("west")
    if(w == e2):
        validDirection.append("east")
    return(validDirection)

def newBlock(north, east, south, west):
    #faces of block to the x
    if north in blocks:
        north = blocks[north]
    else:
        north = blocks["zero"]
    if east in blocks:
        east = blocks[east]
    else:
        east = blocks["zero"]
    if south in blocks:
        south = blocks[south]
    else:
        south = blocks["zero"]
    if west in blocks:
        west = blocks[west]
    else:
        west = blocks["zero"]
    new = (north[2],east[3],south[0],west[1])
    for name, block in blocks.items():
        if (toCardinal(block) == toCardinal(new)):
            return name
    
def newGrid(x,y):
    global entropy, grid, root, window
    if (x>100 or y>100):
        print("grid too big")
    else:
        i = 0
        xAxis = []
        while (i < x):
            yAxis = []
            g = 0
            while (g < y):
                yAxis.append(str(i)+","+str(g))
                g+=1
            xAxis.append(yAxis)
            i+=1
        grid = xAxis.copy()
        entropy = copy.deepcopy(grid)
    root = Tk()
    root.title("Ben Keil #1 Greatest Coder")
    root.geometry("500x500")
    window = Canvas(root, width=width*x, height=width*y)
    window.pack(pady=25)
    printGrid()
    
def printGrid():
    window.delete('all')
    i_count = 0
    for i in grid:
        j_count = 0
        for j in i:
            x1=j_count*width
            y1=i_count*width
            x2=x1+width
            y2=y1+width
            #window.create_rectangle(x1,y1,x2,y2)
            if j in blocks:
                s = Shapes(window, x1, y1, width)
                e = getattr(s,j)
                e()
            else:
                collapse(i_count,j_count)
                window.create_text(((x1+(width/2)),(y1+(width/2))), text=len(entropy[i_count][j_count]))
                window.create_rectangle(x1,y1,x2,y2)
            #z = j + " "
            #z = entropy[i_count][j_count]
            #print(z[:3], end="  ")
            j_count += 1
        #print(" ")
        i_count += 1
    
def insert(block,x,y):
    block = blocks[block]
    for name, i in blocks.items():
        if (toCardinal(block) == toCardinal(i)):
            grid[x][y] = name
            entropy[x][y].clear()
            return name
    printGrid()
    
def collapse(x,y):
    valid = list(blocks.keys())
    if (x-1 >= 0):
        north = grid[x-1][y]
    else:
        north = "zero"
    try:
        east = grid[x][y+1]
    except IndexError:
        east = "zero"
    try:
        south = grid[x+1][y]
    except IndexError:
        south = "zero"
    if (y-1 >= 0):
        west = grid[x][y-1]
    else:
        west = "zero"
    if north in blocks:
        for k,v in blocks.items():
            direction = Compare(v, north)
            if "south" not in direction:
                try:
                    valid.remove(k)
                except:
                    pass
    if east in blocks:
        for k,v in blocks.items():
            direction = Compare(v, east)
            if "west" not in direction:
                try:
                    valid.remove(k)
                except:
                    pass
    if south in blocks:
        for k,v in blocks.items():
            direction = Compare(v, south)
            if "north" not in direction:
                try:
                    valid.remove(k)
                except:
                    pass
    if west in blocks:
        for k,v in blocks.items():
            direction = Compare(v, west)
            if "east" not in direction:
                try:
                    valid.remove(k)
                except:
                    pass
    entropy[x][y] = [*set(valid)]

def fill(x,y):
    valid = []
    for i in entropy[x][y]:
        if i == "one" or i == "two" or i == "four" or i == "eight":
            valid.append(i)
        else:
            valid.append(i)
            valid.append(i)
    insert(random.choice(valid),x,y)
    printGrid()

def find():
    g = 17
    g_list = []
    i_count = 0
    for i in entropy:
        j_count = 0
        for j in i:
            if (len(j) < g and len(j) > 0):
                g_list = []
                g = len(j)
                g_list.append((i_count,j_count))
            elif (len(j) == g):
                g_list.append((i_count,j_count))
            j_count += 1
        i_count += 1
    x,y = random.choice(g_list)
    fill(x,y)


def finish():
    try:
        while True:
            find()
    except:
        pass

def run():
    z = 20
    newGrid(z,z)
    insert("fifteen",4,4)
    i = 0
    while i < z*z-1:
        find()
        i += 1

def displayBlocks():
    newGrid(9,9)
    insert("zero",1,1)
    insert("one",1,3)
    insert("two",1,5)
    insert("three",1,7)
    insert("four",3,1)
    insert("five",3,3)
    insert("six",3,5)
    insert("seven",3,7)
    insert("eight",5,1)
    insert("nine",5,3)
    insert("ten",5,5)
    insert("eleven",5,7)
    insert("twelve",7,1)
    insert("thirteen",7,3)
    insert("fourteen",7,5)
    insert("fifteen",7,7)
    print("zero,   one,      two,      three\nfour,   five,     six,      seven\neight,  nine,     ten,      eleven\ntwelve, thirteen, fourteen, fifteen")
    printGrid()


