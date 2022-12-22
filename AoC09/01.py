class Sznur:
    def __init__(self):
        self.pocz=[0,0]
        self.kon=[0,0]
        self.odwiedzone=set()

    def ile_odwiedzil(self):
        return len(self.odwiedzone)

    def gdzie_odwiedzil(self):
        return self.odwiedzone

    def poziomo(self):
        if ( (self.pocz[1] == self.kon[1]) and (self.pocz[0] != self.kon[0]) ):
            return True
        else:
            return False


    def pionowo(self):
        if ((self.pocz[0] == self.kon[0]) and (self.pocz[1] != self.kon[1])):
            return True
        else:
            return False

    def dlugosc(self):
        return max(abs(self.pocz[0]-self.kon[0]),abs(self.pocz[1]-self.kon[1]))

    def lewo(self):
        if (self.dlugosc() == 0):
            self.odwiedzone.add(tuple(self.kon))
            self.pocz-=1
            self.odwiedzone.add(tuple(self.kon))
        elif (self.dlugosc() == 1 and self.poziomo()):
            self.odwiedzone.add(tuple(self.kon))
            self.pocz[0]-=1
            self.kon[1]-=1
            self.odwiedzone.add(tuple(self.kon))
        elif (self.dlugosc() == 1 and self.pionowo()):
            self.odwiedzone.add(tuple(self.kon))
            self.pocz[0]=self.pocz[0]-1
            self.odwiedzone.add(tuple(self.kon))
        #skos
        else:
            self.odwiedzone.add(tuple(self.kon))
            self.pocz[0]-=1
            self.kon[1]=self.pocz[1]
            self.odwiedzone.add(tuple(self.kon))





sznurek=Sznur()
sznurek.pocz[0]=1
sznurek.pocz[1]=1

print(sznurek.pocz, sznurek.kon)

print(sznurek.dlugosc())
print(sznurek.pionowo())
print(sznurek.poziomo())

sznurek.odwiedzone.add(tuple([0,0]))

print(sznurek.lewo())
print(sznurek.gdzie_odwiedzil())

print(sznurek.lewo())
print(sznurek.gdzie_odwiedzil())

print(sznurek.lewo())
print(sznurek.gdzie_odwiedzil())
