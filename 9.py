import operator

def sortDict(origDict):
    return sorted(origDict.items(), key=operator.itemgetter(1), reverse=True)

def maxDict(origDict):
    k = max(origDict, key=origDict.get)
    return (k, origDict[k])

def minDict(origDict):
    k = min(origDict, key=origDict.get)
    return (k, origDict[k])

with open('9.txt') as f:
    s = f.readlines()

s = [x.strip().split(' ') for x in s][0]
print s


'''
doubly linked circ linked list from https://www.sanfoundry.com/python-program-implement-circular-doubly-linked-list/
'''
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
 
 
class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None
 
    def get_node(self, index):
        current = self.first
        for i in range(index):
            current = current.next
            if current == self.first:
                return None
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        self.insert_after(ref_node.prev, new_node)
 
    def insert_at_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)
 
    def insert_at_beg(self, new_node):
        self.insert_at_end(new_node)
        self.first = new_node
 
    def remove(self, node):
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next
 
    def display(self):
        if self.first is None:
            return
        current = self.first
        s = ''
        while True:
            s += str(current.data) + ' '
            current = current.next
            if current == self.first:
                break
        print s


circ = CircularDoublyLinkedList()
# circ.insert_at_beg(head)
# circ.insert_at_beg(head2)
# circ.display()


numplayers = int(s[0])
maxpt = int(s[6])

print numplayers, maxpt

scores = [0]*numplayers
print scores

marbles = circ
head = Node(0)
marbles.insert_at_end(head)

cur = marbles.get_node(0)

#numplayers, maxpt = 9, 26

maxpt *= 100


for i in range(1, maxpt): #maxpt
    if i%10000 == 0:
        print i
    #print scores
    pnum = i%numplayers # player number
    if i%23 == 0:
        scores[pnum] += i
        for k in range(7):
            cur = cur.prev
        #print 'a', marbles
        scores[pnum] += cur.next.data
        marbles.remove(cur.next)

        #print 'b', marbles
        continue

    cur = cur.next.next
    marbles.insert_after(cur, Node(i))
    #marbles.display()

m = max(scores)
print scores.index(m), m

