from itertools import combinations

def calculate_sum_of_max_elements(arr, size):
    if size <= 0 or size > len(arr):
        return 0  # Invalid size
    
    sum_max_elements = 0

    for combination in combinations(arr, size):
        max_element = max(combination)
        sum_max_elements += max_element

    return sum_max_elements

# Example usage with the array [1, 2, 3, 4, 5, 6] and size 2
array_example = [30, 65, 95, 59, 46, 32, 90, 53, 32, 39, 41, 64, 38, 10, 35, 12, 73, 26, 45, 13, 77, 38, 15, 91, 34, 99, 25, 100, 42, 21]
size_example = 10
sum_max_elements_example = calculate_sum_of_max_elements(array_example, size_example)

print("Sum of maximum elements:",sum_max_elements_example)

