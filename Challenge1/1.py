def resFreq(freq):
    dic = {0: ''}
    currFreq, flag = 0, True
    while(flag):
        for num in freq:
            currFreq += num 
            if currFreq in dic:
                flag = False
                return (currFreq)
            else:
                dic[currFreq] = '' 


f = open("1.txt", "r")
freq = f.readlines()
#print(freq)
temp = []
for x in range(len(freq)-1):
    temp.append(int(freq[x][:-1]))
temp.append(int(freq[-1]))

print(resFreq(temp))