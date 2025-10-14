def check_pass(password):
    is_valid=True
    if len(password)<=8:
        print("the password cannot be less than 8 characters")
        is_valid=False
    if not any(char.isupper() for char in password):
        print("password must contain atleast one uppercase letter")
        is_valid=False
    if not any(char.islower() for char in password):
        print("password must contain atleast one lower case letter")
        is_valid=False
    if not any(char.isdigit() for char in password):
        print("password must contain atleast one digit")
        is_valid=False
    if is_valid:
        print("Password Is Valid")
    else:
        print("Password Is Not Valid!")
    return is_valid
if __name__=="__main__":
  print(check_pass(input("Enter The Password:")))