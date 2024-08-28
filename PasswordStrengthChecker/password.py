#This is a program that checks the strength of a password
import string

password = input("Enter your password please: ")

def check_password_strength(password):
    common_password = ["abcdef" , "123456789","0000000","password","qwertyuiop"]

    if len(password) < 8:
        print("Weak! :Password should have more than 8 characters..")
    if password in common_password:
        return "Weak! :Password is too common therefore vulnerable to malicious attacks.."
    if " " in password:
        return "Weak! :Password should not have any spaces.."

    #checking for uppercase,lowercase,digits and special characters in the password
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)