def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Test the function with your list
strings = ["query1", "query2", "query3", "query4"]
result = longest_common_prefix(strings)
print("Common Prefix:", result)
