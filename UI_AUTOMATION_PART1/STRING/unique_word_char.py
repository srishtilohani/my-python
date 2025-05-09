# sentence = "the flower is red, the tree is green, the snow is white"
# words = sentence.split()
# uniqueword = []
#
# for word in words:
#     if word not in uniqueword:
#         uniqueword.append(word)
#
# print(uniqueword)
#
# input = "aabbccddeeffgg"
# uni_ch = []
#
# for chr in input:
#     if chr not in uni_ch:
#         uni_ch.append(chr)
#
# print(uni_ch)

sentence = "the flower is red, the tree is green, the snow is white"
words = sentence.split()
uniqueword = ""

for word in words:
    if word not in uniqueword:
        uniqueword += word

print(uniqueword)


input = "aabbccddeeffgg"
uni_ch = ""
for chr in input:
    if chr not in uni_ch:
        uni_ch += chr

print(uni_ch)