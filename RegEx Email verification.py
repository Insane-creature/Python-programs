# Email verifier using RegEx 
# RegEx is regular expression is a sequence of characters that specifies a search patterns in text. Is uses varies combination of operations. 

# For email verification here I am applying several conditions such as the first letter input must be a aplhabet between a - z and not a number.
# a -z
# 0-9

# Second condition is there must be either a single '.' or '_' in the input mail ID
# And it should be one time
# . _ 1time

# the '.' should be from last index value 2 or 3 
# . 2,3 from last
# There must be only 1 @ and it is mandatory
# @ 1 time

 
import re

# Following conditions for verification
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

# User input STDIN
user_email = input("Enter your mail ID: ")

# Conditional statement to verify whether it satisfy or not
if re.search(email_condition,user_email):
    print("Correct mail ID")
else:
    print("Wrong email ID")