import numpy as np
file1=open("https://drive.google.com/file/d/1moayugJ1QE8WaLgrDCDrn9jyMCM-nEzR/view?usp=sharing.txt","r")
lista=list()
listb=list()
x=(file1.read()).split('/n')
x.pop(-1)
for i in x:
    listb.append(i.split(" "))
a=listb[0][0]
b=int(listb[0][1])
listb.pop(0)
derayeha=[item for any in listb for item in any]
a=int(a)
b=int(b)
for i in range(len(derayeha)):
    derayeha[i]=int(derayeha[i])


matris=np.array(derayeha).reshape((a,b,b))
detmax=-1000
matrismax=None
for i in range (a):
    for j in range(i+1,a):
        tmpdet=np.linalg.det(np.dot(matris[i]),matris[j])
        if tmpdet>detmax:
            detmax=tmpdet
            matrismax=(matris[i],matris[j])
for i in range(a):
    for j in range(i+1,a):
        tmpdet=np.linalg.det(np.dot(matris[j],matris[i]))
        if tmpdet>detmax:
            detmax=tmpdet
            matrismax=(matris[j],matris[i]) 


if np.linalg.det(matrismax[0])>=np.linalg.det(matrismax[1]):
    javab=np.linalg.inv(np.dot(matrismax[0],matrismax[1]))
else:
    javab=np.linalg.inv(np.dot(matrismax[1],matrismax[0]))

javab=javab.tolist()
for i in javab:
    for j in i:
        print(round(j,3),end=" ")
    print('/n')

