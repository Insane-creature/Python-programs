def is_palindrome(s):
    return s == s[::-1]

s = "mom"
print(is_palindrome(s))