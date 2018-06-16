myList = [ele*2 for ele in range(10) if (ele%2)]
print (myList)

count = 0
febList = [count+ele for ele in range(10)]

print(febList)

for ele in febList:
    count = count+ele
    print(count)