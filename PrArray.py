import array
from random import random
decimalni=array.array('d',(random() for i in range(10**7)))
#prvi argument u funkciji 'typecode' šifra tipa elemenata
with open('PrAr.bin','wb') as bf:
	decimalni.tofile(bf)
#čuvanje na binarnom fajlu
print(decimalni[100:110])
decimalni2=array.array('d',())
with open('PrAr.bin','rb') as bf:
	decimalni2.fromfile(bf,10**7)
#čitanje sa -II- -II-
print(decimalni2[100:110])
#https://docs.python.org/3/library/array.html