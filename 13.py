a=int(input())
b=int(input())
l=int(input())
c=(b<<32)+a
for index in range(l):
    x=int(input())
    if ((2**x)&c):
        print('yes')
    else:
        print('no')
