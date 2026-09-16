import re

code = input("Enter book code: ")

pattern = r'^[A-Z]{3}-[0-9]{4}-[0-9]{3}$'

if re.match(pattern, code):
    print("Valid book code")
else:
    print("Invalid book code")