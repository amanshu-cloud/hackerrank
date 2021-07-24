def rotate(grid,k):
    print(grid[k:] + grid[:k])


n = int(input())
grid = []
for i in range(n):
    j = list(map(int,input().split()))
    grid.append(j)

for g in grid:
    rotate(g,1)
