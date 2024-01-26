def ayaavalastyakheyr(adad):
    if adad <= 1:
        return False
    for i in range(2, int(adad ** 0.5) + 1):
        if adad % i == 0:
            return False
    return True

a, b = map(int, input().split())

tedadadadaval= 0
if a<=b:
    for i in range(a,b+1):
        if ayaavalastyakheyr(i)==True:
            tedadadadaval+=1
    print('main order - amount: '+str(tedadadadaval))
if a>b:
    for i in range(b,a+1):
        if ayaavalastyakheyr(i)==True:
            tedadadadaval+=1
    print('reverse order - amount: '+str(tedadadadaval))