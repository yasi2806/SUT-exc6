i = 0
j = 0
n = int(input())
radif1 = []
result = []

for a in range(n):
    radif1.append('.')
for a in range (1000):
    yasi = radif1.copy()
    result.append(yasi)

result[i][j] ='*'
masir = input()

while masir != "END":
    if masir=="L":
        if i-1>=0:
            i-=1
        else:
            i=0
    elif masir=="R":
        if i < n-1:
            i+=1
        else:
            i = n-1
    
    elif masir=="B":
        j += 1
    result[j][i] ="*"
    masir=input()

while True:
    if radif1 in result:
        result.pop(result.index(radif1))
    else:
        break

for x in range (len(result)):
    for y in range(n):
        print(result[x][y],end=" ")
    print("\n")

if i!=n-1:
    print("There's no way out!")