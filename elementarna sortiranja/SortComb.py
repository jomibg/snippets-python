def shrinkGap(k):
	#eksperimentalno dokazano da je alg. najbrži kad:
	#se faktor smanjuje 1.3 puta
	#kad se umesto faktora 9 i 10 koristi 11 
	k=int(k/1.3)
	if k<1:
		k=1
	return k
def CombSort(arr):
	issorted=False
	k=len(arr)
	while not issorted:
		k=shrinkGap(k)
		#sortitranje umetanjem
		swapoccured=False
		for j in range(0,len(arr)-k):
			if arr[j]>arr[j+k]:
				t=arr[j+k]
				arr[j+k]=arr[j]
				arr[j]=t
				swapoccured=True
		issorted=not swapoccured and k==1
if __name__ == '__main__':
	arr=[4,3,5,7,1]
	print(arr)
	CombSort(arr)
	print(arr)




