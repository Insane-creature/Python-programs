def reverse_string(s):
    return s[::-1]

s = "anshika"
print(reverse_string(s))

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char+reversed_str      # eH
    return reversed_str

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: !dlroW ,olleH
