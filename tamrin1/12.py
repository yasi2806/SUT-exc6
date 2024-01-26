a=int(input())
b=int(input())
e=int(input())
for i in range(32):
    c=a
    d=b
    a=(c&d)<<1
    b=c^d
print(b)
if b==e:
    print("YES")
else:
    print("NO")
    