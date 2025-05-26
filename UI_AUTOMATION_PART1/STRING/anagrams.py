from collections import defaultdict
def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        # Sort the string and use it as a key
        sorted_str = ''.join(sorted(s))
        anagram_map[sorted_str].append(s)

    return list(anagram_map.values())
# Example usage
input_strs = ["cat", "dog", "god", "tca"]
output = group_anagrams(input_strs)
print(output)

def find_anagrams(word_list):
    anagram_dict = defaultdict(list)

    # Group words by sorted characters
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)

    # Print anagram groups with more than one word
    for words in anagram_dict.values():
        if len(words) > 1:
            print("Anagram group:", words)
# Example usage
words = ["listen", "silent", "enlist", "rat", "tar", "art", "dog", "god", "hello"]
find_anagrams(words)
