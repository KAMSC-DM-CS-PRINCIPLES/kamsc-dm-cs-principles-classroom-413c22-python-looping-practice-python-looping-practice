# TODO create reverse string function
# HINT: Use for i in range(len(text) - 1, -1, -1): to go backwards
# HINT: Build reversed_text character by character: reversed_text += text[i]
# HINT: Start with reversed_text = ""
# HINT: Return the reversed_text
# HINT: NO SLICING ALLOWED - must use loops only -> fine



def reverse_string(n: str) -> str:
    r: str = ""
    for char in n:
        r = char + r # prepend each char to reverse the str
    return r
