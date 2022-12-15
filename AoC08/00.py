zakr=99
maks=1
x=1
y=1
def czt (a,b,c,d):
    return a*b*c*d

for i in range(1,zakr):
    for j in range(1,zakr):
        if (czt(zakr-i,i,zakr-j,j)> maks):
            maks=czt(zakr-i,i,zakr-j,j)
            (x,y)=(i,j)

print(maks, x, zakr-x, y, zakr - y)