from multiprocessing import Process


def loop_a(a,b):
    global t1
    t1 = list()
    for i in range(a,10,b):
        t1.append(i)
    print(t1)

def loop_b(c,d):
    global t2
    t2 = list()
    for i in range(c,10,d):
        t2.append(i)
    print(t2)


if __name__=="__main__":
    a = int(input(":"))
    b = int(input(":"))
    c = int(input(":"))
    d = int(input(":"))

    Process(target=loop_a(a,b)).start()
    Process(target=loop_b(c,d)).start()

if len(t1)<len(t2):
    for i in range(len(t1)):
        if t1[i]==t2[i]:
            print("YES")
            break
        else:
            print("NO")

else:
    for i in range(len(t2)):
        if t1[i]==t2[i]:
            print("YES")
        else:
            print("O")