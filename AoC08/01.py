#f = open('input-small.txt', 'r')
f = open('input.txt', 'r')
bok=99
#bok=5
widoczne=2*bok + 2*(bok-2)
print(widoczne)
calosc=[]

#Wczytaj
for line in f:
        arr = list(line)
        arr.pop()
        calosc.append(arr)
#---------
for rzad in range(1,(bok-1)):
    for kolumna in range(1,(bok-1)):
        zaslania_gora=0
        zaslania_dol=0
        zaslania_lewo=0
        zaslania_prawo=0
        print('drzewo@',rzad,kolumna,'=',calosc[rzad][kolumna])
        #gora
        for licz in range(1,rzad+1):
            if (calosc[rzad-licz][kolumna] >= calosc[rzad][kolumna]):
                zaslania_gora=1
                print("gora zaslania     ",calosc[rzad-licz][kolumna])
            else:
                print("gora nie zaslania ",calosc[rzad-licz][kolumna])
        #dol
        for licz in range(1,bok-rzad):
            if (calosc[rzad+licz][kolumna] >= calosc[rzad][kolumna]):
                zaslania_dol=1
                print("dol zaslania     ",calosc[rzad+licz][kolumna])
            else:
                print("dol nie zaslania ",calosc[rzad+licz][kolumna])
        #prawo
        for licz in range(1,bok-kolumna):
            if (calosc[rzad][kolumna+licz] >= calosc[rzad][kolumna]):
                zaslania_prawo=1
                print("dol zaslania     ",calosc[rzad][kolumna+licz])
            else:
                print("dol nie zaslania ",calosc[rzad][kolumna+licz])
        #lewo
        for licz in range(1,kolumna+1):
            if (calosc[rzad][kolumna-licz] >= calosc[rzad][kolumna]):
                zaslania_lewo=1
                print("lewo zaslania     ",calosc[rzad][kolumna-licz])
            else:
                print("lewo nie zaslania ",calosc[rzad][kolumna-licz])
        if ((zaslania_dol+zaslania_gora+zaslania_lewo+zaslania_prawo)<4):
            widoczne+=1
            print("widoczne@",rzad,kolumna,'=',calosc[rzad][kolumna])
        print("----")
    print("=====")
print(widoczne)
