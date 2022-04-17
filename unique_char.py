from enum import unique


def unique_char(s: str) -> int:
    assert isinstance(s, str), "input not a string as it should"
    s = s.lower()
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    
    first = len(s)
    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1

for s in ["appsilon", "Appsilon Poland", "abcabc"]:
    print(f"Index: {unique_char(s=s)}")