f = open('input.txt', 'r')
#f = open('input-small.txt', 'r')


prior = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26,
    "A":26+1,
    "B":26+2,
    "C":26+3,
    "D":26+4,
    "E":26+5,
    "F":26+6,
    "G":26+7,
    "H":26+8,
    "I":26+9,
    "J":26+10,
    "K":26+11,
    "L":26+12,
    "M":26+13,
    "N":26+14,
    "O":26+15,
    "P":26+16,
    "Q":26+17,
    "R":26+18,
    "S":26+19,
    "T":26+20,
    "U":26+21,
    "V":26+22,
    "W":26+23,
    "X":26+24,
    "Y":26+25,
    "Z":26+26
    }

suma=0
for line in f:
        #print(line.splitlines().split(' ')[1])
        #print(line.splitlines())
        arr = list(line)
        arr.pop()
#        print(arr)
        dlugosc = len(arr)
        ktora=-1
        for i in range(int(dlugosc/2)):
                for j in range(int(dlugosc/2)):
#                    print(arr[i],arr[j+int(dlugosc/2)])
                    if(arr[i] == arr[int(dlugosc/2)+j]):
                        ktora=i
#                    else:
#                        print(arr[i], arr[j])
#        print(arr[ktora], "- ", prior[arr[ktora]])
        suma=suma+(prior[arr[ktora]])
print(suma)