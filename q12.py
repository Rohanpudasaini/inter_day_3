# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrom(text1:str) -> bool:
    return (True if (text1 == text1[::-1]) else  False)

print(is_palindrom("cace"))
    