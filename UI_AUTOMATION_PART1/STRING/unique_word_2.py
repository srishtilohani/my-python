sentence = "the flower is red, the tree is green, the snow is white"
words = sentence.split()
unique_word = []

for word in words:
    if word not in unique_word:
        unique_word.append(word)

print(unique_word)

input2 = "aabbcc"
uni_sne = ""

for ch in input2:
    if ch not in uni_sne:
        uni_sne += ch

print(uni_sne)   # → "abc"

input3 = "aabbcc"
input3.split()
uni_sne1 = []

for ch in input3:
    if ch not in uni_sne1:
        uni_sne1.append(ch)

print(uni_sne1)