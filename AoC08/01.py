f = open('input.txt', 'r')
ile=0
calosc=[]
for line in f:
        ile+=1
        arr = list(line)
        arr.pop()
        calosc.append(arr)

#---------X -

#print(calosc)
#print(ile )