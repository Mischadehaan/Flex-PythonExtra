import os

bestand = open('klasgenoten.txt','r')

tekst_regel = bestand.readlines()

for x in tekst_regel:
    x = x.replace("\n","")
    os.mkdir(x)
    


#tekst_regel = tekst_regel.strip()
