f=open("./input.txt", "r")
s=f.readlines()
p=str(s)
maxsum=0
printnum=0

for line in s:
    try:
        printnum=printnum+int(line)
        print("Adding:", printnum)
    except ValueError:
        print("Sum:",printnum)
        if (maxsum<printnum):
            maxsum=printnum
        printnum=0


print("Maxsum:", maxsum)