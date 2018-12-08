with open('8.txt') as f:
    s = f.readlines()

s = [x.strip().split(' ') for x in s][0]
s = map(lambda e: int(e), s)

#print s

summeta = []

def nodeVal(node):
    #print 'node', node
    total = 0
    numchild, nummeta, metadata, children = node
    if numchild == 0:
        return sum(metadata)
    for i in metadata:
        if i <= numchild:
            #print 'recurse', i, children
            total += nodeVal(children[i-1])
    return total

def addNode(s, start):
    children = []
    metadata = []
    length = 2 # for s[0], s[1]
    numchild, nummeta = s[start], s[start + 1]
    #print start
    if start > len(s):
        return (start, (0, 0, [], []))
    for i in range(numchild):
        #print 'child', i
        node = addNode(s, start + length)
        children.append(node[1])
        length += node[0]
    #print 'so far:',length, children
    for i in range(nummeta):
        meta = s[start + length]
        summeta.append(meta)
        metadata.append(meta)
        length += 1
    
    res = (length, (numchild, nummeta, metadata, children))
    #print 'returning', res
    return res

root = addNode(s, 0)
print root
print sum(summeta)
print nodeVal(root[1])