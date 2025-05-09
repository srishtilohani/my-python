
s = "i am good programer"
words  = s.split()
larger_string = ""
# Code (code to find the largest string):
for i in words:
    if len(i) > len(larger_string):
        larger_string = i
print(larger_string)

# Code (Sorting from largest to smallest using for loop):

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if  len(words[i]) < len(words[j]):
            words[i], words[j] = words[j], words[i]
print("Words from largest to smallest:", words)


# Code (Sorting from smallest to largest using for loop):

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if  len(words[i]) > len(words[j]):
            words[i], words[j] = words[j], words[i]
print("Words from largest to smallest:", words)