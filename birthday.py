def birthdayCakeCandles(ar):
    count = 1
    ar.sort()
    for i in range(len(ar)-1):
        if(ar[i]==ar[i+1]):
            count+=1
    print(count)
birthdayCakeCandles([2,3,4,3])