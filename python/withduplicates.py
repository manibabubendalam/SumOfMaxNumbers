import math

def get_factorial(num1, num2):
	return math.factorial(num1)/(math.factorial(num1-num2) * math.factorial(num2))


def max_element_combination_sum(arr, N):
	M = len(arr)
   	if N > M:
		print("Invalid input: N should be less than or equal to M")
		return
	elif N == M:
		return 1 * arr[M-1]
	else:
		return (get_factorial(M-1, N-1) * arr[M-1] + max_element_combination_sum(arr[:M-1], N))


#int1 = int(input("Enter the first integer: "))
#int2 = int(input("Enter the second integer: "))

# Read an array of numbers
#numbers_str = input("Enter the array of numbers separated by spaces: ")
#numbers = list(map(int, numbers_str.split()))
int1 = 30
int2 = 10
numbers = [30, 65, 95, 59, 46, 32, 90, 53, 32, 39, 41, 64, 38, 10, 35, 12, 73, 26, 45, 13, 77, 38, 15, 91, 34, 99, 25, 100, 42, 21]


result = max_element_combination_sum(sorted(numbers), int2)
print "Sum of maximum elements:",result

