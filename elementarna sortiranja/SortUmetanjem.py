def InsertionSort(arr):
	for i in range(1,len(arr)):
		curr=arr[i]
		j=i-1
		while j>=0 and arr[j]>curr:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=curr

if __name__ == '__main__':
	arr=[4,3,5,7,1]
	print(arr)
	InsertionSort(arr)
	print(arr)
