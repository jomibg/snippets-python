a={1,2,3}# set-elementi nisu numerisani i nema dva ista
# elementa-nalik su na skupove u matematici
b=set()
b.add(4)
b.update({5,6,7})
b.remove(7)
print(a|b)#unija
#{1, 2, 3, 4, 5, 6}
print(a&b)#presek
#set()
print(a-b)# razlika a od b
#{1, 2, 3}
print(a^b)# obostrana razlika 
#(elementi iz a kojih nema u b i obrnuto)
#{1, 2, 3, 4, 5, 6}-u ovom slučaju
