# sentence = "the flower is red, the tree is green, the snow is white"
# words = sentence.replace(",", "").split()  # remove commas and split into words
# duplicate_words = ""
# unique_word = ""
#
# for word in words:
#     if word in unique_word:
#         if word not in duplicate_words:
#             duplicate_words += word
#     else:
#         unique_word += word
#
# print(duplicate_words)
# print(unique_word)

sentence = "the flower is red, the tree is green, the snow is white"
words = sentence.replace(",", "").split()  # remove commas and split into words
duplicate_words = []
unique_word = []

for word in words:
    if word in unique_word:
        if word not in duplicate_words:
            duplicate_words.append(word)
    else:
        unique_word.append(word)

print(duplicate_words)
print(unique_word)
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Step 3: Print only duplicate words with their count
for word, count in word_count.items():
    if count > 1:
        print(f"'{word}': {count}")