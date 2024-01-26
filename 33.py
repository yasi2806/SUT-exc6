import re
x=input()
x=re.sub(r' +',' ',x.strip())
x=re.sub(r"\\n","\n",x)

k=""
x=list(x)
place=[]
temp=0

for i in x:
    if i=="@":
        place.append('@')
        temp+=1
    elif i=='#'and temp>0:
        temp-=1
    else:
        place.append(i)
for esm in place:
    k+=str(esm)
print('Formatted Text: '+k)
