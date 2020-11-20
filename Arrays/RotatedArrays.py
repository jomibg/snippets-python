# for given two arrays containing elements from m to n
# in first array numbers are in successive order
# return True if second array is rotated version of first, and False otherwise

def rotation(arr1,arr2):

	if not len(arr1) == len(arr2):
		return False

	l=len(arr1)
	key=arr1[0]
	key_index=0

	for i in range(l):
		if key == arr2[i]:
			key_index=i
			break

	if key_index == 0:
		return False

	for i in range(l):
		l2index=(i+key_index)%l

		if not arr1[i] == arr2[l2index]:
			return False

	return True

if __name__ == '__main__':
	arr1=[1,2,3,4,5]
	arr2=[3,4,5,1,2]
	print(rotation(arr1,arr2))

	arr3=[2,3,4,5]
	arr4=[5,4,3,2]
	print(rotation(arr3,arr4))

