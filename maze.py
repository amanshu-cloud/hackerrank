#issafe function to check if we have reached the edge cases 
def issafe(r,c,n,maze):
    if r<0 or r>=n:
        return False 
    if c<0 or c>=n:
        return False  
    if maze[r][c]:
        return True
    return False

#solcemaze function 

def solvemaze(maze,i,j,soln,n):
    if i==n-1 and j==n-1:
        soln[i][j]==1
        return True
    if issafe(i,j,n,maze):
        soln[i][j]=1
        if solvemaze(maze,i+1,j,soln,n):
            return True
        if solvemaze(maze,i,j+1,soln,n):
            return True 
        soln[i][j]=0
        return False 

n = int(input("enter n"))
maze = [] 
soln = []
for i in range(n):
    maze.append(list(map(int,input().split())))

for i in range(n):
    j = [0]*n
    soln.append(j)


if solvemaze(maze,0,0,soln,n):
    for i in range(n):
        for j in range(n):
            print(soln[i][j],end = "")


else:
    print("-1")   