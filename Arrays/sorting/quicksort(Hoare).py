# example of quicksort implemetation in python usin Hoares partition
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.INFO)

def partition(arr,l,h,comp):
	logging.info(f'current pivot {arr[0]}')
	pivot=arr[l]
	i=l+1
	j=h
	while i<=j: # repeat process while pointers i and j dont 'pass by' each other
		while i<=h and comp(pivot,arr[i]): i+=1 # while pointer i dont reach last index and comp return True  
		while j>l and not comp(pivot,arr[j]): j-=1 # while pointer j dont reach starting point of i and comp return False
		if i<=j: # at this point we found elements arr[i] and arr[j] that are on reversed sides
			arr[i],arr[j]=arr[j],arr[i] # swap these elements
			i+=1
			j-=1
	logging.info(f'Moving pivot from {l}. to {j}. index')
	arr[l],arr[j]=arr[j],arr[l]
	return j

def _sort(arr,l,h,comp):
	# perform recursive divide and conquer tactic using
	logging.info(f'Performin partition on {arr[l:h+1]}')
	if l<h:
		j=partition(arr,l,h,comp)
		_sort(arr,j+1,h,comp)
		_sort(arr,l,j-1,comp)

def quicksort(arr,comp):
	h=len(arr)-1
	_sort(arr,0,h,comp)

asc=lambda p,e: True if p>e else False #e<p
desc=lambda p,e: True if p<e else False #e>p

if __name__ == '__main__':
	arr=[5,7,9,3,2,4,6,8,10,21,33,31,23,30]
	arr2=[7,5,6,3,2]
	arr3=[8,4,3,5]
	quicksort(arr,asc)
	print(arr)
	quicksort(arr,desc)
	print(arr)
	quicksort(arr2,asc)
	print(arr2)
	quicksort(arr3,asc)
	print(arr3)