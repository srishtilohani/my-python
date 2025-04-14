list1  = [12,55,41,10,3,59]

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            list1 [i], list1[j] = list1[j], list1[i]
print(list1)


list2  = [12,55,41,10,3,59]

for i in range(len(list2)):
    for j in range(i + 1, len(list2)):
        if list2[i] < list2[j]:
            list2 [i], list2[j] = list2[j], list2[i]
print(list2)

