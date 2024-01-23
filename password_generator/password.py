import random
import string

def generate_password(length):
    """
    Generates a random password of the specified length.

    Parameters:
    - length (int): Desired length of the password.

    Returns:
    - str: Randomly generated password.
    """
    # Combine lowercase letters, uppercase letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    """
    Main function to execute the password generator application.
    """
    print("Password Generator")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
