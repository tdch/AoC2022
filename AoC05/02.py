f = open('input.txt', 'r')
#f = open('input-small.txt', 'r')

Cra=[['B','V','S','N','T','C','H','Q'],
['W','D','B','G'],
['F','W','R','T','S','Q','B'],
['L','G','W','S','Z','J','D','N'],
['M','P','D','V','F'],
['F','W','J'],
['L','N','Q','B','J','V'],
['G','T','R','C','J','Q','S','N'],
['J','S','Q','C','W','D','M']]

def drukuj(xCra):
    for x in range(len(xCra)):
        print(x+1, '-' ,xCra[x])
    print('\n')

for line in f:


    arr = line.split(" ")


    if (len(arr)>0):
        if(arr[0] == "move"):
#          ile    arr[1]
#          skad   arr[3]
#          dokad  arr[5]

            arr_temp=[]
            for x in range(int(arr[1])):
                arr_temp.append((Cra[int(arr[3])-1]).pop())
            for x in range(int(arr[1])):
                Cra[int(arr[5])-1].append(arr_temp.pop())


#drukuj(Cra)
b=""
for x in range(len(Cra)):
        b=b+(Cra[x].pop())
print(b)
