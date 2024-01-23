import random #this generates a random number
import string # this is an import of letters

def generate_password(length):
    """
    Generates a random password of the specified length.
    Parameters:
    - length (int): Desired length of the password.

    Returns:
    - str: Randomly generated password.
    """
    #below combines numbers, strings and special characters all together
    characters = string.ascii_letters + string.digits + string.punctuation
    #below generates a random mixture of characters, numbers and strings stored in characters variable
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
