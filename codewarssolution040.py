# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

# The result should also be ordered from highest to lowest.

# Examples:

# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []

def two_highest(arg1):
    sorted_set = sorted(set(arg1), key=int, reverse=True)
    if len(sorted_set) < 2:
        return list(sorted_set)
    highest_values = [sorted_set[0], sorted_set[1]]
    return highest_values


print(two_highest([]))
print(two_highest([1, 1, 1, 1]))
print(two_highest([1, 2, 3, 4, 78, 9, 9]))
