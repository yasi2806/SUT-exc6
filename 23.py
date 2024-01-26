def binbasen(a,b):
    y = "" 
    while a > 0: 
        x = a % b 
        y = str(x) + y
        a //= b 
    return y 


list_aval=[] 

temp1=0 
flage=True

while flage: 
    temp2=0 
    a,b = map(int, input().split()) 
    
    
    if int(a)+int(b)==-2: 
        if temp1>0: 
            print('invalid base!') 
            exit() 
        elif temp1==0: 
            break 
    if b <2 or b>=10: 
            temp1+=1 
    for i in range(1,a+1): 
        if a%i==0: 
            temp2+=(a//i) 
                
                
    list_aval.append(binbasen(temp2, b)) 
        
z = 0 
for i in range(len(list_aval)): 
    z+= int(list_aval[i]) 
print(z)
