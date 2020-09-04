def SelectionSort(arr):
	for i in range(len(arr)-1,0,-1):
		maxI=0
		for j in range(1,i+1):
			if arr[j]>arr[maxI]:
				maxI=j
		if maxI!=i:
			t=arr[i]
			arr[i]=arr[maxI]
			arr[maxI]=t
if __name__ == '__main__':
	arr1=[4,6,7,5]
	print(arr1)
	SelectionSort(arr1)
	print(arr1)