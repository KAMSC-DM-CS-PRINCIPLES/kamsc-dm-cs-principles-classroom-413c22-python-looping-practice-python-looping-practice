def reverse_string(n: str) -> str:
    r: str = ""
    for char in n:
        r = char + r # prepend each char to reverse the str
    return r

