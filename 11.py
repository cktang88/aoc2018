import math

serial = 9435 # serial

board = [[0 for i in range(300)] for j in range(300)]

def hun(n):
    return 0 if n < 100 else int(str(n)[-3:-2]) # get hundreds dig

def calc(x,y):
    id = 10 + x
    power = id * y + serial
    power *= id
    return hun(power) - 5

for y in range(300):
    for x in range(300):
        board[y][x] = calc(x,y)

print board

m = 0
a,b,s = 0,0,0

for size in range(1, 300):
    for y in range(300-size):
        #print y
        for x in range(300-size):
            #for row in board[y:y+3]:
                #print row[x:x+3]
            tmp = sum([sum(row[x:x+size]) for row in board[y:y+size]])
            if tmp > m:
                m = tmp
                a,b,s = x,y,size
                print a,b,m,s

print m, a,b


'''
Generally for solving part 2:
1. realize the board is mostly negatives, therefore smaller size is ideal
2. print intermediary result each time you update max, if haven't updated in long time, guess that :)
3. got lucky personally

'''
        
