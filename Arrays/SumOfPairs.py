# for a number given as argumen,
# and array that consists of integers,
# find unique pairs of integers in that array which sum is argument number
# f.e. [0,1,2,3,4],4 -> (0,4),(1,3)

def num_sum_pairs(arr,n):

	if len(arr)<=1:
		raise Exception('Array is to small!')

	output=set()
	seen=set()

	for e in arr:
		target=n-e

		if not target in seen:
			seen.add(e)

		else:
			output.add((min(e,target),max(e,target)))

	return output

if __name__ == '__main__':
	arr1=[1,2,2,0,3,4]
	print(num_sum_pairs(arr1,4))
	print(num_sum_pairs(arr1,5))

