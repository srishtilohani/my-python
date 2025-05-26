numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number2 = [1, 3, 5, 7, 9, 10, 8, 6, 4, 2]
odd_num = []
even_num = []
# Add odd numbers first
for num in numbers:
    if num % 2 != 0:
        odd_num.append(num)
    else:
        even_num.append(num)

result = odd_num + sorted(even_num, reverse=True)

print("Result:", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_num = [num for num in numbers if num % 2 != 0]
even_num = sorted([num for num in numbers if num % 2 == 0], reverse=True)

result = odd_num + even_num

print(result)

result = {i + 20 : numbers[i] + number2[i] for i in range(min(len(number2), len(number2)))}
print(result)


result1 = [numbers[i] + number2[i] for i in range(min(len(number2), len(number2)))]
print(result1)
