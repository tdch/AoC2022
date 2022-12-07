f = open('input', 'r')

ile=14

def rozne(ktora):
    zbior=set()
    for i in range(ile):
        a=arr[ktora-i]
        zbior.add(a)
        if (len(zbior)>=ile):
            print("xy-",ktora, " -", len(zbior), zbior)
#            print(arr[ktora-ile,ktora],"\n")
            return True
#    print("xn-",ktora, " -", len(zbior),zbior)
#    print(arr[ktora-ile:ktora],"\n")
    return False

for line in f:
        arr = []
        for letter in line:
            arr.append(letter)

gdzie_rozne=0

for x in range(ile,len(arr)):
    if (rozne(x)):
        gdzie_rozne=x
#        print(gdzie_rozne)

tdch_from=gdzie_rozne
print(gdzie_rozne)

zbior=set()
for x in range(tdch_from - ile,tdch_from):
    print(x, "-", arr[x])
    zbior.add(arr[x])
print(len(zbior))

#print(arr)