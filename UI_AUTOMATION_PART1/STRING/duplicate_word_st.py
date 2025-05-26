def find_duplicate_word(text):
    words = text.lower().split()
    seen = set()
    for word in words:
        if word in seen:
            return word
        seen.add(word)
    return None

# Example usage:
sentence = "this is a test and this is simple"
duplicate = find_duplicate_word(sentence)
print(duplicate)
# if duplicate:
#     print(f"The duplicate word is: '{duplicate}'")
# else:
#     print("No duplicate word found.")
