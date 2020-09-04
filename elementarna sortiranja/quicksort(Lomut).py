def partition(arr,l,h,comp):
	pivot=arr[h]
	lte_pivot=l-1
	for i in range(l,h):
		if comp(pivot,arr[i]):
			lte_pivot+=1
			arr[i],arr[lte_pivot]=arr[lte_pivot],arr[i]
	pivot_index=lte_pivot+1
	arr[pivot_index],arr[h]=arr[h],arr[pivot_index]
	return pivot_index

def _sort(arr,l,h,comp):
	if l<h:
		j=partition(arr,l,h,comp)
		_sort(arr,j+1,h,comp)
		_sort(arr,l,j-1,comp)

def quicksort(arr,comp):
	h=len(arr)-1
	_sort(arr,0,h,comp)

asc=lambda p,e: True if p>=e else False #e<=p
desc=lambda p,e: True if p<e else False #e>p

if __name__ == '__main__':
	arr=[5,7,9,3,2,4,6,8,10,21,33,31,23,30]
	quicksort(arr,asc)
	print(arr)
	quicksort(arr,desc)
	print(arr)