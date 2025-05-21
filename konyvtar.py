from nagykonyv import Konyv

class Konyvtar:
    def __init__(self):
        self.konyvek = []
        self.fajl_beolvasas()

    def fajl_beolvasas(self):
    
        with open('konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
            next(forrasfajl)
            #kihagy egy sort
            for sor in forrasfajl:
                adatok = sor.strip().split(';')
                nev = adatok[0]
                szul_ev = int(adatok[1])
                hal_ev = int(adatok[2])
                nemzetiseg = adatok[3]
                cim = adatok[4]
                helyezés = int(adatok[5])

                konyvek.append(Konyv(nev, szul_ev, nemzetiseg, hal_ev, cim, helyezés))
