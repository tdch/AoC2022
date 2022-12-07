f = open('input', 'r')
#pociag=[]

#def przesun(dod):
#    pociag[0]=pociag[1]
#    pociag[1]=pociag[2]
#    pociag[2]=pociag[3]
#    pociag[3]=dod

def rozne(ktora):
    if (arr[ktora]!= arr[ktora-1] and
        arr[ktora-1]!= arr[ktora-2] and
        arr[ktora-2]!= arr[ktora-3] and
        arr[ktora-1]!= arr[ktora-2] and
        arr[ktora]!= arr[ktora-2] and
        arr[ktora]!= arr[ktora-3] and
        arr[ktora-1]!= arr[ktora-3]):
            return True
    else:

             return False

for line in f:
        arr = []
        for letter in line:
            arr.append(letter)
#pociag.append(arr[0])
#pociag.append(arr[1])
#pociag.append(arr[2])
#pociag.append(arr[3])
#print(pociag)
#print(arr[0], arr[1], arr[2])

gdzie_rozne=0

for x in range(3,len(arr)):
    if (rozne(x)):
        gdzie_rozne=x
#        print(gdzie_rozne)

tdch_from=1657
for x in range(tdch_from - 3,tdch_from + 3):
    print(x, "-", arr[x])


#print(arr)