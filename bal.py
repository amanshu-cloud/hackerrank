from collections import Counter
paren = list(map(str,input().split()))
conn = Counter(paren)
if len(set(conn.values())) == 1:
    print(1)
else:
    print(-1)