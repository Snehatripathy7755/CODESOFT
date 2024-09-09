import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the length is positive
    if length < 1:
        raise ValueError("Password length must be at least 1 character.")
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main program
def main():
    try:
        # Prompt the user for the length of the password
        length = int(input("How long would you like your password to be? "))
        
        # Generate the password
        password = generate_password(length)
        
        # Display the password
        print("Your generated password is:", password)
    
    except ValueError as e:
        print(f"Invalid input: {e}")

# Run the program
if __name__ == "__main__":
    main()

