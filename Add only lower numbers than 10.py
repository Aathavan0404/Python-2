aList = [2,3,11,13,5,7]

s = 0

for i in range(len(aList)):
    if(aList[i]>10):
        continue
    s = s + aList[i]
print(s)
        
