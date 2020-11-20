spisak='Petar Perić\nMarko Marković\nPavle Pavlović'
spisak_lista=spisak.split('\n')
ime=slice(0,5)
prezime=slice(6,None)
for ip in spisak_lista:
	_ime=ip[ime]
	_prezime=ip[prezime]
	print(_ime,_prezime)
