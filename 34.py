#by me
kotl = input()



n = int(input())

list1 =kotl.split()

dict1 = dict()

dict2 = dict()

for i,j in enumerate(list1):
    dict1[int(j)]=i


for i in dict1.keys():
    temp = n - i

    if temp in dict1 and temp!=i:
        sum1 = dict1[i]+dict1[temp]

        if (temp,i) not in dict2.keys():
            dict2[(i,temp)]=sum1

natijeh_nahayii = sorted(dict2.values())


if not dict2:
    print("Not Found!")



else:
    for item in natijeh_nahayii:
        print(item)