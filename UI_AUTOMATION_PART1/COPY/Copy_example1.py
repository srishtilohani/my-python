import copy
nested_list = [[1, 2], [3, 4]]
shall_copy = copy.copy(nested_list)
nested_list[0].append(88)
print(nested_list)
print(shall_copy)

deep_copy = copy.deepcopy(nested_list)
nested_list[1].append(87)
print(nested_list)
print(shall_copy)
print(deep_copy)