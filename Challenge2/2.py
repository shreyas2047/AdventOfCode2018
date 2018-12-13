from collections import Counter

def checkSum(c):
    two, three = 0, 0
    for char in c:
        d = Counter(char)
        values = d.values()
        if 2 in values:
            two += 1
        if 3 in values:
            three += 1
        d.clear()
    return two*three

def common(c):
    temp = {}
    for i in range(len(c)):
        for j in range(len(c)):
            if i != j:
                a, b = check(c[i], c[j])
                if a == True:
                    temp[c[i][:b] + c[i][b+1:]] = ''
    return temp.keys()

def check(s1, s2):
    size = len(s1)
    start, end = 0, size
    count = 0
    while start < end:
        if s1[start] != s2[start]:
            count += 1
            index = start
        start += 1
    if count == 1:
        return (True, index)
    return (False, -1)


f = open("2.txt", "r")
temp = f.readlines()
#print(freq)
for x in range(len(temp)-1):
    temp[x] = temp[x][:-1]

ch = ['abcde', 'axcye']
print(common(temp))