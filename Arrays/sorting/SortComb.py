def shrinkGap(k):
	# it's experimentaly prooved that algorithm is quickest when
	# when factor is lowernig for 1.3 times
	# and when instead factors 9 and 10 we use 11 
	k=int(k/1.3)
	if k<1:
		k=1
	return k

def CombSort(arr):
	issorted=False
	k=len(arr)
	while not issorted:
		k=shrinkGap(k)
		#insertion sort
		swapoccured=False
		for j in range(0,len(arr)-k):
			if arr[j]>arr[j+k]:
				arr[j],arr[j+k]=arr[j+k],arr[j]
				swapoccured=True
		issorted=(not swapoccured) and (k==1)
		
if __name__ == '__main__':
	arr=[4,3,5,7,1]
	print(arr)
	CombSort(arr)
	print(arr)




