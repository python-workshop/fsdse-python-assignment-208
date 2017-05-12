def build(string, k):
    if string is None:
        return False
    if k is None:
        return False
    small = 0
    large = 0
    index_map = {}
    for index, char in enumerate(string):
        index_map[char] = index
        if len(index_map) > k:
            small = min(index_map.values())
            del index_map[string[small]]
            small += 1
        large = max(large, index - small + 1)
    return large
value = build("aabbcc",3)
print (value)