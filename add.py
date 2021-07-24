n = int(input())
grid = []
for i in range(n):
    m = list(map(int,input().split()))
    grid.append(m)

steps_dict = {}
if grid[n-1][len(m)-1]==1:
    print("0")
else:
    for i in range(n-1):
        for j in range(len(m)-1):
            #loop to move to the bottom
            if grid[i+1][j]==0:
                steps_dict['top'] = steps_dict.get("top",0)+1
            elif grid[i][j+1]==0:
                steps_dict['down'] = steps_dict.get("down",0)+1
print(steps_dict)
                
