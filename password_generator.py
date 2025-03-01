import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""

    all_characters = lower + upper + numbers + symbols

    if len(all_characters) == 0:
        print("You must select at least one character set.")
        return None

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"

    password = generate_password(length, use_uppercase, use_numbers, use_symbols)

    if password:
        print("\nGenerated Password: " + password)

if __name__ == "__main__":
    main()
