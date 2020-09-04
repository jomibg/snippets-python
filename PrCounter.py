from collections import Counter
c=Counter('aaaabbbcc')
print(c)
#Counter({'a': 4, 'b': 3, 'c': 2})
print(c.most_common(2))# 2-br. traženih elemenata
#po učestalosti
#[('a', 4), ('b', 3)]
print(list(c.elements()))
#['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']
print(c['d'])# ne izbacuje grešku već vrednost 0
d=Counter({'a':1,'b':2,'d':-2})
c.subtract(d)# oduzima svaku vrednost skupa d od c
#pr c.d - d.d = 0 - (-1)=1
print(c)
#Counter({'a': 3, 'c': 2, 'd': 2, 'b': 1})
c.update(d)# subrotno subtractu, sabira elemente
#Counter({'a': 4, 'b': 3, 'c': 2, 'd': 0})
print(c)

# DRUGI NAČINI VRŠENJA MATEMATIČKIH RADNJI NAD ELEMENTIMA
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)                # add two counters together:  c[x] + d[x]
#Counter({'a': 4, 'b': 3})
print(c - d)                # subtract (keeping only positive counts)
#Counter({'a': 2})
print(c & d)                # intersection:  min(c[x], d[x])
#Counter({'a': 1, 'b': 1})
print(c | d)                # union:  max(c[x], d[x])
#Counter({'a': 3, 'b': 2})
