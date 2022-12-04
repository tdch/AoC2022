f=open("./input.txt", "r")
s=f.readlines()
p=str(s)
sumy=[]
printnum=0

for line in s:
    try:
        printnum=printnum+int(line)
        #print("Adding:", printnum)
    except ValueError:
        #print("Sumy:",sumy)
        sumy.append(printnum)
        printnum=0

sumy.sort(reverse=True)
print("Max", sumy[0], sumy[1], sumy[2])
print("Max 3 sum:", sumy[0]+ sumy[1]+ sumy[2])
