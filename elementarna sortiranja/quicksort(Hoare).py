def parititon(arr,l,h,comp):
	pivot=arr[l]
	i=l+1
	j=h
	while i<=j:
		while i<=h and comp(pivot,arr[i]): i+=1
		while j>l and not comp(pivot,arr[j]): j-=1
		if i<=j:
			arr[i],arr[j]=arr[j],arr[i]
			i+=1
			j-=1
	arr[l],arr[j]=arr[j],arr[l]
	return j

def _sort(arr,l,h,comp):
	if l<h:
		j=parititon(arr,l,h,comp)
		_sort(arr,j+1,h,comp)
		_sort(arr,l,j-1,comp)

def quicksort(arr,comp):
	h=len(arr)-1
	_sort(arr,0,h,comp)

asc=lambda p,e: True if p>e else False #e<p
desc=lambda p,e: True if p<e else False #e>p

if __name__ == '__main__':
	arr=[5,7,9,3,2,4,6,8,10,21,33,31,23,30]
	quicksort(arr,asc)
	print(arr)
	quicksort(arr,desc)
	print(arr)