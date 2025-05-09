from collections import Counter

def get_repeated_words(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()

    # Remove punctuation from words
    words = [word.strip(".,!?;:'\"()[]{}") for word in words]

    # Count word occurrences
    word_counts = Counter(words)

    # Filter out words that appear more than once
    repeated_words = {word: count for word, count in word_counts.items() if count > 1}

    return repeated_words

# Example usage
input_text = "This is a test. This test is only a test."
repeated = get_repeated_words(input_text)

print("Repeated words and their counts:")
for word, count in repeated.items():
    print(f"{word}: {count}")
