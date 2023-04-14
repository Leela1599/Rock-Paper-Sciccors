import string

password = input("Enter your password: ")
passowrd_in_list = list(password)

password_checks = ["lowercase", "uppercase", "digits", "special characters"]

lower = 0
upper = 0
digit = 0
special = 0

for char in passowrd_in_list:
    if char in string.ascii_lowercase:
        lower += 1
        if "lowercase" in password_checks:
            password_checks.remove("lowercase")
    elif char in string.ascii_uppercase:
        upper += 1
        if "uppercase" in password_checks:
            password_checks.remove("uppercase")
    elif char in string.digits:
        digit += 1
        if "digits" in password_checks:
            password_checks.remove("digits")
    else:
        special += 1
        if "special characters" in password_checks:
            password_checks.remove("special characters")

print("Your Results")
print("Lowercase " + str(lower))
print ('uppercase ' + str(upper))
print ('Digits ' + str(digit))
print ('Special Characters' + str(special))

if len(passowrd_in_list) <=9:
    print ( "Error: Passowrd is too short. It must be greater than 9 Characters. ")

if len (password_checks) != 0:
    print ("Password is not strong enough.")

if len(password_checks) == 0 and len(passowrd_in_list) > 9:
    print (' Passowrd is strong, save it')