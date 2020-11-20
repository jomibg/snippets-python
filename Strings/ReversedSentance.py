# put words from given string in reverse order
# f.e. This is super -> super is This

def reverseString(s):

	words=[]
	spaces=[' ',]
	i=0
	l=len(s)

	while i<l:
		if s[i] not in spaces:
			word_start=i
			i+=1
			while i<l and s[i] not in spaces:
				i+=1
			word=s[word_start:i]
			words.append(word)
		i+=1

	return ' '.join(reversed(words))

if __name__ == '__main__':
	print(reverseString('This is super'))
