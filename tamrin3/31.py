a=input()
a=a.split(" ")
a.sort(key=lambda a: int(a[1:]))
for i in a:
    print(i[0], end='')