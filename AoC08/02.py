#f = open('input-small.txt', 'r')
f = open('input.txt', 'r')
bok=99
#bok=5
best_score=0
calosc=[]
wyniki=[]

#Wczytaj
for line in f:
        arr = list(line)
        arr.pop()
        calosc.append(arr)
#---------
for rzad in range(1,(bok-1)):
    for kolumna in range(1,(bok-1)):
        widac_gora=1
        widac_dol=1
        widac_lewo=1
        widac_prawo=1
#        current_score=0
        print('drzewo@',rzad,kolumna,'=',calosc[rzad][kolumna])
        #gora
        for licz in range(1,rzad+1):
            if (calosc[rzad-licz][kolumna] < calosc[rzad][kolumna] ):
                widac_gora=licz
                print("gora Nie zaslania     ",calosc[rzad-licz][kolumna])
            else:
                widac_gora+=1
                break

        #dol
        for licz in range(1,bok-rzad):
            if (calosc[rzad+licz][kolumna] < calosc[rzad][kolumna] ):
                widac_dol=licz
                print("dol nie zaslania     ",calosc[rzad+licz][kolumna])
            else:
                widac_dol+=1
                break
        #prawo
        for licz in range(1,bok-kolumna):
            if (calosc[rzad][kolumna+licz] < calosc[rzad][kolumna]):
                widac_prawo=licz
                print("dol Nie zaslania     ",calosc[rzad][kolumna+licz])
            else:
                widac_prawo+=1
                break
        #lewo
        for licz in range(1,kolumna+1):
            if (calosc[rzad][kolumna-licz] < calosc[rzad][kolumna]):
                widac_lewo=licz
                print("lewo zaslania     ",calosc[rzad][kolumna-licz])
            else:
                widac_lewo+=1
                break
        if ((widac_dol*widac_gora*widac_lewo*widac_prawo)>best_score):
            best_score=widac_dol*widac_gora*widac_lewo*widac_prawo
            print("max_score")
        wyniki.append(widac_dol*widac_gora*widac_lewo*widac_prawo)
        print("X:",rzad,kolumna,":",calosc[rzad][kolumna],":",widac_gora,widac_dol, widac_lewo, widac_prawo, "=", widac_dol*widac_gora*widac_lewo*widac_prawo )
        print("----")
    print("=====")
#print(best_score)
wyn_sort=sorted(wyniki)
for i in range(9):
    print(wyn_sort.pop())
#print(wyn_sort)
