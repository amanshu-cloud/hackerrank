'''problem statement
Day 31:[2020-04–15] Problem of the Day! (Asked in Google)

A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four. '''
#solution
new = [listt[i:j] for i in range(len(listt)) for j in range(i+1,len(listt)+1)]
#print(new)

new.sort(key=len)
print(new)
for li in new:
    maxx = len(li)
    dup = []
    for i in range(len(new)):
        if len(new[i])>maxx:
            for ele in new[i]:
                if ele not in dup:
                    dup.append(ele)
            if len(dup)==2:
                output = new[i]
                break

print(output)     
