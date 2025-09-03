def get_char(index):
    letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    symbols = "!@#$%^&*"

    sets = letters + letters.upper() + digits + symbols
    length = len(sets)

    pos = (index * index + index * 7) % length
    return sets[pos]

def generate_password(length):
    password = ""
    for i in range(length):
        ch = get_char(i + length)
        password += ch
    return password

def main():
    print("=== Simple Password Generator ===")
    length_input = input("Enter desired password length: ")

    if not length_input.isdigit():
        print("Invalid input. Please enter a number.")
        return

    length = int(length_input)

    if length <= 0:
        print("Password length must be greater than 0.")
        return

    password = generate_password(length)
    print("Generated Password:", password)

main()