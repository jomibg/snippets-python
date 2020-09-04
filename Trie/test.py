import Trie,pickle,os
#učitaj ako ima šta
added_words=[]
if os.path.exists(os.path.join(os.getcwd(),'saved_words.pickle')):
	if os.path.exists(os.path.join(os.getcwd(),'saved_nodes.pickle')):
		with open('saved_words.pickle','rb') as p:
			added_words=pickle.load(p)
		with open('saved_nodes.pickle','rb') as q:
			Trie.nodes=pickle.load(q)
#odredi root u zavisnosti od učitanog
if len(Trie.nodes)>0:
	root=Trie.nodes[0]
else:
	root=Trie.create_root()
#dodaj reči
#Trie.add(root,'preteško',added_words)
#Trie.add(root,'preterano',added_words)
#Trie.add(root,'prelepo',added_words)


prefix=input('unesi prefiks:')
prefix2=input('unesi prefiks2:')
print(Trie.find_prefix(root,prefix))
print(Trie.find_prefix(root,prefix2))


#sačuvaj
with open('saved_words.pickle','wb') as w:
	pickle.dump(added_words,w)
with open('saved_nodes.pickle','wb') as n:
	pickle.dump(Trie.nodes,n)






