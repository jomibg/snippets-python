#python module which provides heapsort with
#adjustable comparator function
#it relies on max-heap sorting principle
#so elements with higher priority are in higher
#indexes in sorted iterable
from singleton import singleton_decorator

@singleton_decorator
class parent_child(object):
	#object that stores comparator function
	def __init__(self,comp=lambda p,c: True if (p>=c) else False):
		#by default max-heap comparator fnc
		self.comp = comp

	def compare(self,parent,child):
		return self.comp(parent,child)
		#function that compares elements at
		#parent-child indexes

	def determine_son(self,parentI,lastI,arr):
		#function that returns index of son
		#with higher priority
		childI=None
		if parentI*2+1<=lastI:
			childI=parentI*2+1
			if childI+1<=lastI and self.compare(arr[childI+1],arr[childI]):
				childI+=1
		return childI

ParentChild=parent_child()

def heapsort(arr):
	endI=len(arr)-1
	startI=(endI-1)//2
	#heapifying arr from first
	#parent index to the root
	while startI>=0:
		heapify(startI,endI,arr)
		startI-=1
	#swaping element from root(index 0) with element
	#on last index, lowering last index by 1
	#and then restoring heap order from index 0
	#to the last index
	while endI>0:
		arr[0],arr[endI]=arr[endI],arr[0]
		endI-=1
		heapify(0,endI,arr)

def heapify(first,last,arr):
	#restoring heap order of 'branch'
	#from first to last given indexes
	parentI=first
	heapRestored=False
	while not heapRestored:
		maxSonI=ParentChild.determine_son(parentI,last,arr)
		if not maxSonI or ParentChild.compare(arr[parentI],arr[maxSonI]):
			heapRestored=True
		else:
			arr[parentI],arr[maxSonI]=arr[maxSonI],arr[parentI]
			parentI=maxSonI


if __name__ == '__main__':
	a=[5, 7, 9, 1, 3,6,2,7,5,1,1,2,3,4,5,6,7,8,9,10]
	b=[2,3,10,11,25,4,5,6,7,8]
	heapsort(a)
	heapsort(b)
	print(a)
	print(b)