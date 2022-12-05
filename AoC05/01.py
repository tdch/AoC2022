f = open('input.txt', 'r')

C1=['B','V','S','N','T','C','H','Q']
C2=['W','D','B','G']
C3=['F','W','R','T','S','Q','B']
C4=['L','G','W','S','Z','J','D','N']
C5=['M','P','D','V','F']
C6=['F','W','J']
C7=['L','N','Q','B','J','V']
C8=['G','T','R','C','J','Q','S','N']
C9=['J','S','Q','C','W','D','M']



for line in f:
        #print(line.splitlines().split(' ')[1])
        #print(line.splitlines())
        arr = line.split()
        #print(arr)

#---------X -
        if (arr[1] == "X"):
            if (arr[0]=="A"):
                suma=suma+4
            elif (arr[0]== 'B'):
                suma=suma+1
            elif (arr[0]== 'C'):
                suma=suma+7
