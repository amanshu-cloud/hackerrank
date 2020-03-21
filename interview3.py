a = [3,2,1]
print(len(a))
count = 0
while True:
    Swapflags = False
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i] , a[i+1] = a[i+1],a[i]
            count+=1
            print(a)
            Swapflags = True
    if not Swapflags:
        break

print(a)



