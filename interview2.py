count = dict()
list_of_vs = list()
list_of_unique_vs = list()
s = 'aabbcd'
for letters in s:
    count[letters] = count.get(letters,0)+1
print(count)
for k,v in count.items():
    list_of_vs.append(v)
list_of_vs.sort()
for v in list_of_vs:
    if not v in list_of_unique_vs:
        list_of_unique_vs.append(v)
list_of_unique_vs.sort()

if len(list_of_vs)>2:
    if len(list_of_unique_vs)==1:
        Result = "YES"
    elif len(list_of_unique_vs)==2:
        if list_of_unique_vs[0] == list_of_unique_vs[1]-1:
            Result = "Yes"
        else:
            Result = "NO"
    else:
        Result = "NO"


elif len(list_of_vs)<= 2:
    if len(list_of_unique_vs)==1:
        Result = "YES"
    elif len(list_of_unique_vs)==2:
        if list_of_unique_vs[0] == list_of_unique_vs[1]-1:
            Result = "Yes"
        else:
            Result = "NO"


print(Result)
