a=input()
a=int(a)
# print(a)
b=input()
b=int(b)
# print(b)

c=a
bita=[]
while (not c<2):
    # print(c%2)
    bita.append(c%2)
    c=c//2
# print(c)
bita.append(c)
# print(bita)

d=b
bitb=[]
while (d>=2):
    # print(d%2)
    bitb.append(d%2)
    d=d//2
# print(d)
bitb.append(d)
# print(bitb)
# print(len(bitb))

if len(bitb)>len(bita):
    dif=len(bitb)-len(bita)
    for index in range(dif):
        bita.append(0)
else:
    dif=len(bita)-len(bitb)
    for index in range(dif):
        bitb.append(0)




number=0
for index in range(len(bitb)):
    if not  bitb[index]==bita[index]:
        number +=1

print(number)