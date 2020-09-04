# example of Heap implementation in python
class Heap(object):
	def __init__(self,comp):
		self.heap = []
		#list to store items of heap
		self.comp=comp
		#function that check relation between
		#two items of heap and returns True
		#if they ar in parent-child relation
	def __repr__(self):
		return 'Heap({!r})'.format(self.heap)

	def _inv_heapify(self,child_ind):
		#Do heapifying starting from bottom 
		#till it reaches the root.
		heap,compare=self.heap,self.comp
		child=child_ind
		while child > 0:
			parent=(child-1)//2
			#finds index of the parent
			if compare(heap[parent],heap[child]):
			#if compare returns True, two items are
			#in parent-child relation 	
				return 
			heap[parent],heap[child]=heap[child],heap[parent]
			child=parent

	def _heapify(self,parent_ind):
		#Do heapifying starting from root 
		heap,compare=self.heap,self.comp
		length=len(heap)
		if length==1:
			return
		parent=parent_ind
		while parent*2+1<length:
		#ther is surely one child
			child=parent*2+1
			if child+1 < length and compare(heap[child+1],heap[child]):
			#ther is second child with bigger
			#priority than first
				child+=1
			if compare(heap[parent],heap[child]):
				return
			heap[parent],heap[child]=heap[child],heap[parent]
			parent=child

	def heappop(self):
	#returns and removes item with biggest priority
		heap=self.heap
		last=heap.pop()
		if not heap:
			return last
		item=heap[0]
		heap[0]=last
		self._heapify(0)
		return item
    
	def min_or_max(self):
	#returns item with biggest priority
		if not self.heap:
			return None
		return self.heap[0]

	def add(self,element):
		self.heap.append(element)
		self._inv_heapify(len(self.heap)-1)

max_heap=lambda p,c: True if (p>c) else False
min_heap=lambda p,c: True if (p<c) else False

if __name__ == '__main__':
	li = [5, 7, 9, 1, 3]
	h=Heap(max_heap)
	for e in li:
		h.add(e)
	print(h)
	h2=Heap(min_heap)
	for e in li:
		h2.add(e)
	print(h2)
	print(h2.heappop())









		