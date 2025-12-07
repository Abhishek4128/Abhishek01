import re
password = input("Enter password: ")

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
print("Valid" if re.match(pattern, password) else "Invalid")
