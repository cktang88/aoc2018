

with open('1.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content]
sums = dict()
sums[0] = True
sum = 0
buffer = content
found = False
while (len(buffer) > 0) and not found:
    for c in buffer:
        sum += c
        if sum not in sums:
            sums[sum] = True
        else:
            print('good', sum)
            found = True
            break
    # keep looping
    buffer = content
    print(len(sums))

