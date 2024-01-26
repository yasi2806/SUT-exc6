mode=input()
def lcd(a,b):
    return abs(a*b)//gcddadeha(a,b) 
def gcddadeha(a,b):
    while b!=0:
        a,b=b,a%b
    return a
if mode=="sum": 
    jaamevorudiha=0 
    while True: 
        vorudi= input() 
        if vorudi == 'end': 
            break 
        jaamevorudiha+=int(vorudi) 
    print(jaamevorudiha) 
    
elif mode == 'average': 
    voroodi1=0 
    voroodi2=0 
    while True: 
        vorudi=input() 
        if vorudi=='end':
            break 
        voroodi1+=int(vorudi) 
        voroodi2+=1 
        miangin=voroodi1/voroodi2 
    print(round(miangin, 2))
elif mode == 'max':
    lista= []
    while True: 
        a = input()
        if a=='end': 
            break 
        lista.append(int(a)) 
    print(max(lista)) 
elif mode == 'min':
    b = float('inf')
    while True:
        ab = input() 
        if ab == 'end':
            break 
        a1 = int(ab)
        b = min(b, a1) 
    print(b)


    
elif mode=="gcd":
    listadad=[]
    while True:
        dadeha=input()
        if dadeha=="end":
            break
        listadad.append (int(dadeha))
    while len(listadad)!=1:
        bmm=gcddadeha(listadad[0],listadad[1])
        x=listadad[0]
        y=listadad[1]
        listadad.remove(x)
        listadad.remove(y)
        listadad.append(bmm)
    print (listadad[0])





elif mode=="lcd":
    listadad=[]
    while True:
        dadeha=input()
        if dadeha=="end":
            break
        listadad.append(int(dadeha))
    while len(listadad) != 1:   
        kmm=lcd(listadad[0],listadad[1])
        x=listadad[0]
        y=listadad[1]
        listadad.remove(x)
        listadad.remove(y)
        listadad.append(kmm)
    print (listadad[0])
else:
    print("Invalid command")
