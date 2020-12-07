'''
Attempt #2 (12/6/2020), completed solution.
'''

inp = open('10.txt','r')
arr = [l.strip() for l in inp]
res = 0
pts = []
vs = []
for r in arr:
  p,v = r.split('> velocity=<')
  p = [int(i) for i in p.split('<')[1].split(',')]
  v = [int(i) for i in v.split('>')[0].split(',')]
  pts.append(p)
  vs.append(v)

tot = 1_000_000

for i in range(100000):
  oldpts = [p[:] for p in pts]
  for pi,p in enumerate(pts):
    p[0] += vs[pi][0]
    p[1] += vs[pi][1]
  minx = min(p[0] for p in pts)
  maxx = max(p[0] for p in pts)
  miny = min(p[1] for p in pts)
  maxy = max(p[1] for p in pts)
  newtot = (maxy + maxx - miny - minx)
  if newtot > tot:
    print(tot, newtot)
    # rollback
    pts = oldpts
    break
  else:
    tot = newtot
print(i)
# for p in plots
for i in range(miny, maxy):
  s=''
  for j in range(minx, maxx):
    s += '@' if [j,i] in pts else ' '
  print(s)

'''
Original 2018 attempt (failed to get solution)
'''

# with open('10.txt') as f:
#     s = f.readlines()

# s = [x.strip() for x in s]
# def process(e):
#     e = e[10:]
#     k = e.split('>')
#     a = [int(e) for e in k[0].split(',')]
#     b = [int(e) for e in k[1][12:].split(',')]
#     return a,b

# s = map(process, s)
# print len(s)
# print s

# minx = min(s, key=lambda e: e[0][0])[0][0]
# maxx = max(s, key=lambda e: e[0][0])[0][0]
# miny = min(s, key=lambda e: e[0][1])[0][1]
# maxy = max(s, key=lambda e: e[0][1])[0][1]
# print minx, maxx, miny, maxy

# board = [["." for i in range(minx, maxx + 1)] for j in range(miny, maxy + 1)]

# def setCoord(coord, newchar):
#     #print coord
#     y,x = coord[1], coord[0]
#     if y < miny or x < minx or x > maxx or y > maxy:
#         return
#     board[y - miny][x-minx] = newchar

# def update():
#     # update
#     for e in s:
#         #print e
#         # reset old pos
#         setCoord(e[0], ".")
#         e[0][0] += e[1][0]
#         e[0][1] += e[1][1]
#         # set new pos
#         setCoord(e[0], "#")

# def printboard():
#     # print
#     for i in range(0, maxy - miny + 1):
#         print "".join(board[i])
#     print "\n"

# for e in s:
#     setCoord(e[0], "#")
# printboard()

# import time
# while True:
#     update()
#     printboard()

#     time.sleep(100)
