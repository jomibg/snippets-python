# for given array count biggest continuous sum
# (sum consisting of successive elements)
# array can contain positive and negative integers

def max_continuous_sum(arr):
	print(f'Counting max sum for {arr}:')

	if len(arr) == 0:
		raise Exception('Array must contain at least one element')

	current_sum=max_sum=arr[0]
	print(f'current element is {current_sum}')

	for i in range(1,len(arr)):
		print(f'current element is {arr[i]}')
		current_sum=max(current_sum+arr[i],arr[i])
		print(f'current sum is {current_sum}')
		max_sum=max(max_sum,current_sum)
		print(f'current max sum is {max_sum}')

	return current_sum

if __name__ == '__main__':
	arr=[1,2,3,-3,7,-10,5,6]
	print(max_continuous_sum(arr))