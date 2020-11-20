# You ar given array that represent queue of people
# We think of numbers in arrays as numbers of initial position of each person in queue
# Each person can bribe persons most two people so each person can get most two positions in front of initial position
# So ou are given array consisting of successive numbers from 1 to n ,which elements are shuffled
# Your goal is to count number of 'bribes' that have happened in this 'queue'

def num_of_bribes(arr):

	queue=enumerate([ e-1 for e in arr])

	bribes=0

	for i,p in queue:
		if p-i > 2:
			raise Exception('Array is too chaotic')

		for j in range(max(p-1,0),i):
			if arr[j]>p:
				bribes+=1

	return bribes

if __name__ == '__main__':
	
	q1=[2,1,5,3,4]
	q2=[2,5,1,3,4]
	print(num_of_bribes(q1))
	print(num_of_bribes(q2))


