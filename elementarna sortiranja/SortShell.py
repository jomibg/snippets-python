def ShellSort(arr):
	k=int(len(arr)/2.25)
	if k==0:
		k=1
	while k>0:

		#formiranje podskupova u razmacima dužine k
		for i in range(0,k):

			#sortiranje umetanjem
			for j in range(i+k,len(arr),k):
				curr=arr[j]
				previndex=j-k
				while previndex>=0 and arr[previndex]>curr:
					arr[previndex+k]=arr[previndex]
					previndex-=k
				arr[previndex+k]=curr	
		if k==2:
			k=1
		else:
			k=int(k/2.25)
if __name__ == '__main__':
	arr1=[4,6,7,5]
	print(arr1)
	ShellSort(arr1)
	print(arr1)


				


