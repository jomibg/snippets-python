def ExchangeSort(arr):
	for i in range(len(arr)-1,0,-1):
		swapoccured=False
		for j in range(0,i):
			if arr[j]>arr[j+1]:
				t=arr[j+1]
				arr[j+1]=arr[j]
				arr[j]=t
				swapoccured=True
		if not swapoccured:
			break
if __name__ == '__main__':
	arr=[4,3,5,7,1]
	print(arr)
	ExchangeSort(arr)
	print(arr)

		
