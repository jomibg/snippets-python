import bisect
ocene=[1,2,3,4,5]
granice=sorted([60,80,70,90])
rezultat=65
def oceni(rez):
	i=bisect.bisect(granice,rez)
	return ocene[i]
print(oceni(rezultat))
#2
bisect.insort(granice,65)
print(granice)
	