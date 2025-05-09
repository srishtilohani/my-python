# List of numbers provided
numbers = [1, 2, 3, [4, 5], 6]

# Flatten the list and sum all numbers
flattened_numbers = [item for sublist in numbers for item in (sublist if isinstance(sublist, list) else [sublist])]
sum_of_numbers = sum(flattened_numbers)

print(sum_of_numbers)
