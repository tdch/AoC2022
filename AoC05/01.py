f = open('input.txt', 'r')

C1=[['B','V','S','N','T','C','H','Q'],
['W','D','B','G'],
['F','W','R','T','S','Q','B'],
['L','G','W','S','Z','J','D','N'],
['M','P','D','V','F'],
['F','W','J'],
['L','N','Q','B','J','V'],
['G','T','R','C','J','Q','S','N'],
['J','S','Q','C','W','D','M']]


linenr=0
for line in f:
    linenr+=1
        #print(line.splitlines().split(' ')[1])
        #print(line.splitlines())
        print(line)
        arr = line.split()
        print(linenr, arr[1])

#---------X -
        if (arr[0] == "move"):
                print(arr[1], arr[3], arr[5])
