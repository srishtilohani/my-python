list1  = [12,55,41,10,3,59]
max_num = float('-inf')
second_num = float('-inf')
third_num = float('-inf')
soerted_list = sorted(list1)
print(soerted_list)

for num in list1:
    if num > max_num:
        max_num = num
print("max_number_in_list", max_num)

for num in list1:
    if num != max_num and num > second_num:
        second_num = num
print(second_num)

for num in list1:
    if num != max_num  and  num != second_num and  num > third_num:
        third_num = num
print(third_num)



