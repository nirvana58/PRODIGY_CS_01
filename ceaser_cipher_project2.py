def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 97) % 26 + 97)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

mode = input("Choose mode ('encrypt' or 'decrypt'): ").lower()
if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
    exit()

user_text = input("Enter your message: ")
shift_value = int(input("Enter the shift value (positive for encryption, negative for decryption): "))

encrypted_text = caesar_cipher(user_text, shift_value, mode)
print("Result:", encrypted_text)
