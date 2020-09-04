from collections import namedtuple
Card=namedtuple('Card',['rank','suit'])
Kraljtref=Card(13,'tref')
print(Kraljtref)
#Card(rank=12,suit='tref')
print(Kraljtref.suit)
#tref
print(Card._fields)
#('rank', 'suit')
data=[13,'pik']
Kraljpik=Card._make(data)
print(Kraljpik)