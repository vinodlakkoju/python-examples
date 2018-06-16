def feb(num):
    f1= 0
    f2= 1
    febList = []
    for i in range(num ):
        f = f1+f2
        f1=f2
        f2=f
        febList.append(f)
    return febList
l = feb(20)
print(l)
print(feb(10))