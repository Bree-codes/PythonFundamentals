#This is a program that checks the strength of a password
import string

password1 = input("Enter the Password to be Checked: ")

def check_password_strength(password):
    common_password = ["abcdef" , "123456789","0000000","password","qwertyuiop"]

    if len(password) < 8:
        print("Weak! Password should have more than 8 characters.")
    if password in common_password:
        return "Weak! Password is too common, therefore vulnerable to malicious attacks."
    if " " in password:
        return "Weak! Password should not have any spaces."

    #checking for uppercase,lowercase,digits and special characters in the password
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if not has_special:
        return "Weak! Password must contain at least 1 special character[!,@,#,$,%,&,*,^]"
    if not has_upper:
        return "Weak! Password must contain at least 1 uppercase character."
    if not has_lower:
        return "Weak! Password must contain at least 1 lowercase character."
    if not has_digit:
        return "Weak! Password must contain at least 1 digit."

    if len(password) >= 10 and has_upper and has_lower and has_digit and has_special:
        return "Strong!"
    else:
        return "Moderate!"

strength = check_password_strength(password1)
print(strength)


