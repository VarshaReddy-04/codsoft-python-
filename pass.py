import random
import string

def generate_password(length):
    
    letters = string.ascii_letters  
    digits = string.digits
    special_chars = string.punctuation
    
    all_characters = letters + digits + special_chars
    
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    while True:
        
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length must be at least 1.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        
        password = generate_password(length)
        
    
        print(f"Generated password: {password}")
        
    
        again = input("Do you want to generate another password? (yes/no): ")
        if again.lower() != 'yes':
            break
    
    print("Thank you for using the password generator!")

if __name__ == "__main__":
    main()
