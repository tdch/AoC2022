f = open('input-small.txt', 'r')
suma=0
arr=[]
drzewo= {
    "name" : "a",
    "size" : 2,
    "type" : "file",
    "content": []
}

drzewo2 = {'name': '/', 'size': -1, 'type': 'dir', 'content': [drzewo, drzewo]}

def pokazdrzewo(wciecie,drzewko):
    if (drzewko["type"] == "file"):
        print(wciecie, drzewko["name"], drzewko["size"])
    else:
        print(wciecie, drzewko["name"])
        w=len(drzewko["content"])
        if (len(drzewko["content"]) >= 1):
            for x in range(len(drzewko["content"])):
                pokazdrzewo(wciecie+"+--",drzewko["content"][x])
#    for key, value in drzewko.items():
#        if   (key == 'file'):
#            print(wciecie,key, ' : ', value)
#        elif (key == 'dir'):
#            pokazdrzewo(wciecie + "+--", value)


def pracuj(komenda, drzewo):
    if   (komenda[0].isnumeric()):
        pracuj_tworz_plik(komenda[1],drzewo)
    elif (komenda[0] == "dir"):
        pracuj_tworz_dir(komenda[1],drzewo)
    elif (komenda[0] == "cd"):
        pracuj(komenda[1], drzewo[komenda[1]])



for line in f:
        #print(line.splitlines().split(' ')[1])
        #print(line.splitlines())
        arr = line.split()
        print(arr[0])
#        pracuj(sciezka,arr)


print(drzewo2)
print("1\n")

#pokazdrzewo("--",drzewo)
#print("2\n")

pokazdrzewo("--",drzewo2)
print("3\n")