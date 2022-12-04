f = open('input.txt', 'r')
#f = open('input-small.txt', 'r')

suma=0
for line in f:
        arr = line.rstrip('\n').split(',')
        pocz1=int(arr[0].split('-')[0])
        kon1=int(arr[0].split('-')[1])
        pocz2=int(arr[1].split('-')[0])
        kon2=int(arr[1].split('-')[1])
        #print(pocz1,kon1,pocz2,kon2)
        if ((pocz1<=pocz2) and (kon1>=kon2)):
            print("yes1-",pocz1,kon1,pocz2,kon2)
            suma=suma+1
        elif ((pocz2<=pocz1) and (kon2>=kon1)):
            print("yes2-",pocz1,kon1,pocz2,kon2)
            suma=suma+1
        else:
            print("no  -",pocz1,kon1,pocz2,kon2)
        #print(arr)


print(suma)