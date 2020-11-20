# HackerRank SHerlock and anagrams
# find number of anagramic substrings in each string 
#anagramic -> which are built of exactly same letters (order of letters isnt important)
# i. e. kkkk has 10 pairs
# k,k,k,k -> six pairs (combinations of 2 letters in diferent positions)
# kk,kk -> 2 pairs
# kkk,kkk -> 2 pairs
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.INFO)

def CountPairs(s):

	logging.info(f'Counting pairs of anagrams in string {s}')
	count=dict()

# find all substring and add them to count
	for i in range(1,len(s)):
		logging.info(f'Creating {i} letters anagrams:')
		for j in range(0,len(s)-i+1):
			ss=''.join(sorted(s[j:j+i]))
			if ss in count:
				count[ss]+=1
			else:
				count[ss]=1
			logging.info(f'{ss} added to {count}')

# sum of numbers of combinations for each substring
	return sum(sum(range(a)) for a in count.values())

if __name__ == '__main__':
	e1='kkkk'
	e2='ifailuhkqq'
	print(CountPairs(e1))
	print(CountPairs(e2))