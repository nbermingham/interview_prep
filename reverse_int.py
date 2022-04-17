def reverse_int(n: int) -> int:
    """
    reverses the integer n
    """
    assert isinstance(n, int), "input is not integer"
    if n < 0:
        neg = True
        n *= -1
    else:
        neg = False
    
    s = str(n)
    revstr = ""

    for i in range(len(s)-1, -1, -1):
        revstr += s[i]

    rev = int(revstr)
    if neg:
        rev *= -1
    
    return rev

print(reverse_int("asdfh"))
    