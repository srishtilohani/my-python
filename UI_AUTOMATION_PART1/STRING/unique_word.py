sentence = "the flower is red, the tree is green, the snow is white"
words = sentence.split()  # Split sentence into words
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("Unique words:")
for word in unique_words:
    print(word)

sentence = "the flower is red, the tree is green, the snow is white"
words = sentence.split()  # Split sentence into words
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("Unique words as list:")
print(unique_words)
