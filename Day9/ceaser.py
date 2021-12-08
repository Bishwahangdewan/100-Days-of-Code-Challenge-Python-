# ceaser_cipher
import art

alphabets = ['a', 'b', 'c', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['$', '(', ')', '#', '%', '&']

print(art.cipher_art)

restart = True


def start(re):
    while re:

        direction = input("Type 'encrypt' to encode , 'decrypt to decode : \n")

        if direction == 'encrypt':
            inputs(direction)
        elif direction == 'decrypt':
            inputs(direction)
        else:
            print("Invalid Input")

        start_again = input("Type 'yes' if you want to go again otherwise type 'no' ")
        if start_again == 'yes':
            re = True
        else:
            re = False



def ceasar(shift, text, direction):
    encoded_or_decoded_text = ''
    for text_letter in text:

        if text_letter == ' ':
            encoded_or_decoded_text += ' '

        for number in numbers:
            if text_letter == number:
                encoded_or_decoded_text += number

        for symbol in symbols:
            if text_letter == symbol:
                encoded_or_decoded_text += text_letter

        for alphabet_index in range(len(alphabets) - 1):
            if text_letter == alphabets[alphabet_index]:
                if direction == 'encrypt':
                    encoded_or_decoded_text += alphabets[(alphabet_index + shift) % 26]
                else:
                    encoded_or_decoded_text += alphabets[alphabet_index - shift]

    print(f"The changed text is {encoded_or_decoded_text}")


def inputs(direct):
    text = input("Type your message to encrypt").lower()
    shift = int(input("Type the shift number"))
    ceasar(shift, text, direct)


start(restart)
