# Get input from user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create an empty string to store the result
reversed_sentence = ""

# Use a for loop to go through the words in reverse (using reversed())
for word in reversed(words):
    reversed_sentence += word + " "

# Print the result after stripping extra space
print("Reversed sentence:", reversed_sentence.strip())
# Program to reverse a word using a for loop

word = input("Enter a word: ")
reversed_word = ""

# Loop through each character in the word
for char in word:
    reversed_word = char + reversed_word  # Prepend each character

print("Reversed word:", reversed_word)

def get_unique_words(text):
    words = text.split()
    unique_words = ' '.join([word for word in words if words.count(word) == 1])
    return unique_words

# Example
input_text = "this is"
output = get_unique_words(input_text)
print("Unique words:", output)
