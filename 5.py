with open('5.txt') as f:
    s = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
#s = [x.strip().split(' ') for x in s]
s = s[0].strip()
#s = 'dabAcCaCBAcCcaDA'
print(s)
print(len(s))

def react(s):
    i = 1
    while i < len(s):
        #print i
        if s[i].lower() == s[i-1].lower() and s[i] != s[i-1]:
            #print(s)
            try:
                s = s[:i-1] + s[i+1:]
            except Exception as e:
                print e
            i -= 2
            if i < 1:
                i = 0
            #print s, i
        i +=1
    return len(s)

alpha = 'abcdefghijklmnopqrstuvwxyz'
d = dict()
for i in alpha:
    print i
    new = s.replace(i, '').replace(i.upper(), '')
    d[i] = react(new)
print d
print min(d, key=d.get)
