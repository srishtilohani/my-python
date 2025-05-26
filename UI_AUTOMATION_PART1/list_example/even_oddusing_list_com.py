numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [f"{num} is even" if num %2 == 2 else f"{num} is odd" for num in numbers]
print(result)