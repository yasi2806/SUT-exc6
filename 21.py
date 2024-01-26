n = int(input())
list1= []
for i in range(n):
    temp1 = []
    for j in range(i+1):
        if j==0 or j==i:
            temp1.append(1)
        else:
            temp1.append(list1[i-1][j-1]+list1[i-1][j])
    list1.append(temp1)

for x in range(n):
    for y in range(len(list1[x])):
        print(list1[x][y],end=' ')
    print('\n')
