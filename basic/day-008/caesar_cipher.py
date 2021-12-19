from arts import logo

def caesar(message: str, shift: int, decode: bool = False) -> str:
    caesar_text = ""
    for char in message:
        if char not in ALPHABET:
            caesar_text += char
        else:
            index = ALPHABET.index(char) + shift if not decode else ALPHABET.index(char) - shift
            caesar_text += ALPHABET[index]

    return caesar_text

ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo)

should_continue = True
while should_continue:

    option = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
    message = input("Enter with your message: ").lower()
    shift_number = int(input("Type the Shift number: "))
    # Using module to solve the larger shift problem (because the alphabet has only 26 letters)
    shift_number = shift_number % 26

    if option == "encode":
        encoded_message = caesar(message=message, shift=shift_number)
        print(f"Here's the encoded result: {encoded_message}")

    elif option == "decode":
        decoded_message = caesar(message=message, shift=shift_number, decode=True)
        print(f"Here's the decoded result: {decoded_message}")

    else:
        print("Invalid option.")

    should_continue = input("Do you want to continue? (y/n): ").lower()
    if should_continue == "n":
        should_continue = False
        print("Goodbye!")
