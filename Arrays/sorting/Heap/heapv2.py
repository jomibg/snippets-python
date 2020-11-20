import heapq
#implementation of heap using pythons module heapq
#only minimum heap is provided
class Heap(list):
    def __init__(self, heap=None):
        if heap is None:
            heap = []
        heapq.heapify(heap)
        super(Heap, self).__init__(heap)

    def __repr__(self):
        return 'Heap({})'.format(super(Heap, self).__repr__())

    def push(self, item):
        return heapq.heappush(self, item)

    def heappop(self):
        return heapq.heappop(self)

    def pushpop(self, item):
        return heapq.heappushpop(self, item)

    def replace(self, item):
        return heapq.heapreplace(self, item)

    def nlargest(self, n, *args, **kwargs):
        return heapq.nlargest(n, self, *args, **kwargs)

    def nsmallest(self, n, *args, **kwargs):
        return heapq.nsmallest(n, self, *args, **kwargs)

if __name__ == '__main__':
    li = [5, 7, 9, 1, 3]
    h2=Heap(li)
    print(h2)
    print(h2.heappop())