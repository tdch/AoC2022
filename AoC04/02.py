f = open('input.txt', 'r')
#f = open('input-small.txt', 'r')

suma=0
liczba_linii=0
for line in f:
        liczba_linii +=1
        arr = line.rstrip('\n').split(',')
        pocz1=int(arr[0].split('-')[0])
        kon1 =int(arr[0].split('-')[1])
        pocz2=int(arr[1].split('-')[0])
        kon2 =int(arr[1].split('-')[1])
        if ((kon1<pocz2)):
            print("yes1-",pocz1,kon1,pocz2,kon2)
            suma=suma+1
        elif ((kon2<pocz1)):
            print("yes2-",pocz1,kon1,pocz2,kon2)
            suma=suma+1
        else:
            print("no  -",pocz1,kon1,pocz2,kon2)


print("Trafione:",suma)
print("Reszta:", liczba_linii - suma)