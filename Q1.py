# 1. Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# 2. Find average of all elements in the list
def find_average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

# 3. Multiply each element by a scalar value
def multiply_by_scalar(lst, scalar):
    return [item * scalar for item in lst]

# Testing Question 1
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Original List:", numbers)
print("Remove Duplicates:", remove_duplicates(numbers))
print("Find Average:", find_average(numbers))
print("Multiply by Scalar (2):", multiply_by_scalar(numbers, 2))