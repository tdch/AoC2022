class Tabela:
    def __init__(self):
        self.pusty=0
        self.tabelka=[ [self.pusty] ]
        self.rzedow=1
        self.kolumn=1


    def powieksz_z_lewej(self, ile):
        for rzad in range(self.rzedow):
            for kolumna in range(ile):
                self.tabelka[rzad].insert(0,self.pusty)
                self.kolumn+=1

    def powieksz_z_prawej(self, ile):
        for rzad in range(self.rzedow):
            for kolumna in range(ile):
                self.tabelka[rzad].append(self.pusty)
                self.kolumn+=1

    def powieksz_z_gory(self, ile):
        for iter in range(ile):
            tmp=[]
            for kolumna in range(self.kolumn):
                tmp.append(self.pusty)
            self.tabelka.insert(0,tmp)
            self.rzedow+=1

    def powieksz_z_dolu(self, ile):
        for iter in range(ile):
            tmp=[]
            for kolumna in range(self.kolumn):
                tmp.append(self.pusty)
            self.tabelka.append(tmp)
            self.rzedow+=1

    def wypisz(self):
        print("wymiary:", self.rzedow, self.kolumn)
        for rzad in range(self.rzedow):
            for kolumna in range(self.kolumn):
                print(self.tabelka[rzad][kolumna])
            print("---")
        print("=====")

tabliczka=Tabela()
tabliczka.tabelka[0][0]=1
tabliczka.wypisz()
tabliczka.powieksz_z_prawej(2)
tabliczka.powieksz_z_lewej(2)
tabliczka.wypisz()
tabliczka.powieksz_z_dolu(2)
tabliczka.powieksz_z_gory(2)
tabliczka.wypisz()
