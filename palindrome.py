def is_palindrome_1(s: str) -> bool:
    return s == s[::-1]

def is_palindrome_2(s:str) -> bool:
    return s == ''.join(reversed(s))

def is_palindrome_3(s: str) -> bool:
    if len(s) <= 1:
        return True
    return is_palindrome_3(s[1:-1]) and s[0] == s[-1] 

print(is_palindrome_1("annbna"))
print(is_palindrome_2("annbna"))
print(is_palindrome_3("anna"))