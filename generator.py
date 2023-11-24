import string
import random


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)

        password += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password


min_length = int(input("Enter the Length of Password: "))
has_number = input("Do you want numbers in your password (y/n)? ").lower() == "y"
has_special = (
    input("Do you want special characters in your password (y/n)? ").lower() == "y"
)
password = generate_password(min_length, has_number, has_special)
print("The Generated Password is:", password)
