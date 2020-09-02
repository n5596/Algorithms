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

def FastSelect(A, k):
	n = len(A)

	if n <= 5:
		A_sort = quicksort(A)
		return A[k-1]
	i = 0
	G = []
	S = []
	while i < n:
		temp_list = A[i:i+6]
		G.append(temp_list)
		temp_sort = quicksort(temp_list)
		if len(temp_sort) == 5:
			S.append(temp_sort[2])
		else:
			index = int(len(temp_sort)/2)
			S.append(temp_sort[index])
		i += 6
	p = FastSelect(S, int(n/10))
	A1 = []; A2 = []; A3 = []
	for val in A:
		if val < p:
			A1.append(val)
		elif val > p:
			A3.append(val)
		else:
			A2.append(val)
	if k <= len(A1):
		return FastSelect(A1, k)
	elif len(A1) < k and k <= len(A1) + len(A2):
		return p
	else:
		kval = k-len(A1)-len(A2)
		return FastSelect(A3, kval)
	

n = np.random.randint(1000)
A_original = np.random.randint(1000, size = n)

print('Finding the median of A_original')
s1 = time.time()
k = n/2
median = FastSelect(A_original, int(k))
e1 = time.time()
print('Found the median ', median, 'in ', e1-s1, 'seconds')
print('Numpy median is ', np.median(A_original))
