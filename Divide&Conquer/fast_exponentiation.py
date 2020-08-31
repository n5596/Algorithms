import numpy as np
import time
import copy

def naive(a, n):
	c = copy.copy(a)
	for i in range(1, n):
		c = c*a
	return c

def fast_exponentiation(a, n):
	if n == 1:
		return a
	if n % 2 == 0:
		x = fast_exponentiation(a, n/2)
		return x*x
	else:
		x = fast_exponentiation(a, (n-1)/2)
		return a*x*x
	
n = np.random.randint(1000)
a = np.random.randint(1000)
print('Testing with a = ', a, 'and n = ', n)
print('TESTING NAIVE APPROACH')
s1 = time.time()
p1 = naive(a, n)
e1 = time.time()
print('Time taken for naive approach = ', e1-s1)
print('TESTING DIVIDE AND CONQUER')
s2 = time.time()
p2 = fast_exponentiation(a, n)
e2 = time.time()
print('Time taken for divide and conquer approach = ', e2-s2)

if p1 == p2:
	print('Results match')
else:
	print('Results mismatch')
