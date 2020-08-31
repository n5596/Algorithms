import numpy as np
import time 
import copy

def quicksort(A):
	n = len(A)
	if n <= 1:#base case
		return A 
	mid = round(n/2)

	pivot = A[mid]
	A1 = []; A2 = []; A3 = [];
	for i in range(n):
		if A[i] < pivot:
			A1.append(A[i])
		elif A[i] > pivot:
			A3.append(A[i])
		elif A[i] == pivot:
			A2.append(A[i])
	A1_sort = quicksort(A1)
	A3_sort = quicksort(A3)
	sort_A = A1_sort + A2 + A3_sort
	return sort_A

n = np.random.randint(1000)
A_original = np.random.randint(1000, size = n)
s1 = time.time()
A_sort = quicksort(A_original)
e1 = time.time()

A_before = copy.copy(A_original)
A_original.sort()
A_original = list(A_original)

if A_original == A_sort:
	print('Sorted array matches inbuilt function.')
else:
	print('Mismatch with inbuilt function.')

#print('Original Array: \n', A_before)
#print('Original Array sorted with inbuilt function: \n', A_original)
#print('Sorted Array: \n', A_sort)
print('Time taken for quicksort:', e1-s1)
