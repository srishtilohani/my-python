sentanse = "srishti is my name my name is srishti"
duplicate_word = []
unique_word = []
word_count = {}
words = sentanse.split()
for word in words:
    if word not in unique_word:
        unique_word.append(word)
    else:
        duplicate_word.append(word)
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(unique_word)
print(duplicate_word)
print(word_count)

sent = "aabbccccccccccccccccccccccccccccddeeffgghh"
duplicate_word1 = []
unique_word1 = []
word_count1 = {}

for char in sent:
    if char not in unique_word1:
        unique_word1.append(char)
    else:
        duplicate_word1.append(char)
print(unique_word1)
print(duplicate_word1)

for count in sent:
    if count in word_count1:
        word_count1[count] += 1
    else:
        word_count1[count] = 1
print(word_count1)