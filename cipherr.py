from cipher_alphabets import alphabet

should_continue = True
while should_continue:
    print("CAESAR CIPHER")
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26   # controls shift if given large number than 26

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position+shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"The {cipher_direction}d text is {end_text}")

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Do you you wanna go again? Type (Y/N): \n").lower()
    if result == "n":
        should_continue = False
        print("Goodbye")
    elif result == "y":
        should_continue = True
    else:
        print("Invalid Command")
