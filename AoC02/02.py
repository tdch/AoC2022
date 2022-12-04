f = open('input.txt', 'r')
suma=0
for line in f:
        #print(line.splitlines().split(' ')[1])
        #print(line.splitlines())
        arr = line.split()
        #print(arr)

#---------X -
        if (arr[1] == "X"):
            if (arr[0]=="A"):
                suma=suma+3
            elif (arr[0]== 'B'):
                suma=suma+1
            elif (arr[0]== 'C'):
                suma=suma+2

        if (arr[1] == "Y"):
            if (arr[0]=="A"):
                suma=suma+4
            elif (arr[0]== 'B'):
                suma=suma+5
            elif (arr[0]== 'C'):
                suma=suma+6

        if (arr[1] == "Z"):
            if (arr[0]=="A"):
                suma=suma+8
            elif (arr[0]== 'B'):
                suma=suma+9
            elif (arr[0]== 'C'):
                suma=suma+7
print(suma)