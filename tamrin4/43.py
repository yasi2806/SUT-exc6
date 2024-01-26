
try:
    khatha = list()
    for i in range(6):
        x = input()
        khatha.append(x)
    
    

    lista ,listb = khatha[0].split(' ')
    listb = listb.strip()
    list1 , list2 = khatha[1].split(' ')
    list1 = int(list1)
    list2 = int(list2)
    dicA , dicB , dicC = khatha[2].split(' ')
    damagecard = {'A':dicA,'B':dicB,'C':dicC}
    p1points = 0
    p2points = 0
    

    for i in range(3,6):
        tmpcardp1 ,tmpcardp2 = khatha[i].split(' ')
        if int(damagecard[tmpcardp1[0]]) > int(damagecard[tmpcardp2[0]]):
            p1points += 1
        elif int(damagecard[tmpcardp2[0]]) > int(damagecard[tmpcardp1[0]]):
            p2points += 1
        list1 -= int(damagecard[tmpcardp2[0]])
        list2 -= int(damagecard[tmpcardp1[0]])
    print(lista + " -> Score: "+str(p1points)+', Health: '+str(list1))
    print(listb + " -> Score: "+str(p2points)+', Health: '+str(list2))
   


except:
    print('Invalid Command.')
        
