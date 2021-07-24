def knap(W,weight,value,n):
    if n==0 or W==0:
        return 0
    if weight[n-1] > W:
        return knap(W,weight,value,n-1)
    else:
        return max(value[n-1]+ knap(W-weight[n-1],weight,value,n-1),knap(W,weight,value,n-1))


W = int(input())
weight = list(map(int,input().split()))
values = list(map(int,input().split()))
n =len(weight)
print(knap(W,weight,values,n))  
