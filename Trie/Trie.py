nodes=[]
class TrieNode:
	def __init__(self,char):
		self.char=str(char)
		self.children=[]
		self.word_finished=False
		self.counter=1

def create_root(): 
	root=TrieNode('')
	nodes.append(root)
	return root

def add(root,word,added_words=[]):
	if len(str(word))>0 and word not in added_words:
		node=root
		for char in word:
			found_in_child=False
			for child in node.children:
				if child.char==char:
					child.counter+=1
					node=child
					found_in_child=True
					break
			if not found_in_child:
				new_node=TrieNode(char)
				node.children.append(new_node)
				nodes.append(new_node)
				node=new_node
		node.word_finished=True
		added_words.append(word)

def find_prefix(root,prefix):	
	node=root
	if not root.children:
		return False,0
	for char in prefix:
		char_not_found=True
		for child in node.children:
			if child.char==char:
				char_not_found=False
				node=child
				break
		if char_not_found:
			return False,0
	return True, node.counter

def find_pattern(root,pattern):
	node=root
	for char in pattern:
		char_not_found=True
		for child in node.children:




		