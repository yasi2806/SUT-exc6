set1=set()
n=int(input())

for _ in range(n):
    inp1=input()
    if "@" in inp1:
        _,domain=inp1.split("@",1)
        set1.add(domain)
javab=sorted(set1)
for item in javab:
    print(item)