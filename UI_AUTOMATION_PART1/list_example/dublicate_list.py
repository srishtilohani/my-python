sent = [1, 1, 1, 2, 3, 34, 44, 421, 33, 33]
duplicate_word1 = set()
unique_word1 = set()
word_count1 = {}

for num in sent:
    if num not in unique_word1:
        unique_word1.add(num)
    else:
        duplicate_word1.add(num)

print("Unique words (numbers):", unique_word1)
print("Duplicate words (numbers):", duplicate_word1)

for word in sent:
    if word in word_count1:
        word_count1[word] += 1
    else:
        word_count1[word] = 1

print("Word count:", word_count1)
