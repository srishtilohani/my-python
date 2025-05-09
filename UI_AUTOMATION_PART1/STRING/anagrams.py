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
