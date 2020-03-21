matrix = []
sum_1 = 0
sum_2 =0

for i in range(3):
    a = int(input('i:'))
    for j in range(1):
        b=int(input("j:"))
        for k in range(1):
            c = int(input("k:"))
            matrix.append([a,b,c])

for i in range(3):
    sum_1 +=matrix[i][i]
    sum_2+=matrix[len(matrix)-1-i][i]

print(matrix)
print(sum_1,sum_2)