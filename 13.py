
with open('13.txt') as f:
    s = f.readlines()

board = []
for line in s:
    row = []
    for c in line:
        if c =='\n':
            continue
        row.append(c)
    board.append(row)

print board
for i in board:
    print len(i)
print len(board)

cars = [] # list of tuples (car, intersection-move)

# moves: left, straight, up = 0,1,2
moves = ['^','>','V','<']

for i, row in enumerate(board):
    for j, c in enumerate(row):
        if c == '>' or c == '<' or c == '^' or c == 'v':
            cars.append((i,j,-1)) # start off left

print cars

update = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0, -1)}


import operator
def addtuple(a,b):
    return tuple(map(operator.add, a, b))

while True:
    cars.sort() # sort by pos (col, row)
    for c in cars:
        i,j,move = c
        
        sym = board[i][j]
        newi, newj = addtuple(update[sym], (i,j))
        nxt = board[newi][newj]
        if nxt == '+':
            # intersection
            newmove = (move + 1) % 3
        elif nxt == '\\':
            if sym == '<':
                sym = '^'
            else:
                sym = '>'
        elif nxt == '/':
            if sym == '>':
                sym = '^'
            else:
                sym = '<'
        else:
            i,j = newi, newj
        c = (newi, newj, newmove)
    print cars
    break
        
