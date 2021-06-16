import time
import os
def clear(): return os.system("cls")


beastcodeencrypt = {
    'A': 'f',
    'B': 'A',
    'C': 'W',
    'D': '*',
    'E': 'L',
    'F': 'G',
    'G': '6',
    'H': 'o',
    'I': 'n',
    'J': 'z',
    'K': '"',
    'L': '<',
    'M': 'e',
    'N': 'V',
    'O': 'p',
    'P': 'k',
    'Q': '~',
    'R': 'X',
    'S': 'Z',
    'T': '=',
    'U': '3',
    'V': '8',
    'W': '(',
    'X': 'U',
    'Y': 'D',
    'Z': ':',
    'a': '|',
    'b': 'y',
    'c': 's',
    'd': 'm',
    'e': '_',
    'f': 'H',
    'g': 'Q',
    'h': 'T',
    'i': '[',
    'j': '.',
    'k': ')',
    'l': 'h',
    'm': 'J',
    'n': 'M',
    'o': '#',
    'p': '4',
    'q': ',',
    'r': '?',
    's': 't',
    't': 'R',
    'u': 'C',
    'v': 'x',
    'w': 'v',
    'x': '{',
    'y': 'K',
    'z': '1',
    '1': '2',
    '2': 'a',
    '3': '7',
    '4': 'b',
    '5': '`',
    '6': '+',
    '7': '}',
    '8': '&',
    '9': '>',
    '0': ';',
    '@': '/',
    '#': 'i',
    '$': '!',
    '_': ']',
    '&': '-',
    '-': 'F',
    '+': '@',
    '(': 'q',
    ')': 'j',
    '/': 'B',
    '*': 'c',
    '"': 'Y',
    ':': '^',
    ';': '$',
    '!': 'O',
    '?': '5',
    '~': 'E',
    '`': 'I',
    '|': 'l',
    '^': '%',
    '=': 'u',
    '{': 'g',
    '}': '0',
    '%': 'S',
    '[': 'N',
    ']': '9',
    '<': 'P',
    '>': 'r',
    '.': 'd',
    ',': 'w',
    ' ': ' '
}

beastcodedecrypt = {
    'f': 'A',
    'A': 'B',
    'W': 'C',
    '*': 'D',
    'L': 'E',
    'G': 'F',
    '6': 'G',
    'o': 'H',
    'n': 'I',
    'z': 'J',
    '"': 'K',
    '<': 'L',
    'e': 'M',
    'V': 'N',
    'p': 'O',
    'k': 'P',
    '~': 'Q',
    'X': 'R',
    'Z': 'S',
    '=': 'T',
    '3': 'U',
    '8': 'V',
    '(': 'W',
    'U': 'X',
    'D': 'Y',
    ':': 'Z',
    '|': 'a',
    'y': 'b',
    's': 'c',
    'm': 'd',
    '_': 'e',
    'H': 'f',
    'Q': 'g',
    'T': 'h',
    '[': 'i',
    '.': 'j',
    ')': 'k',
    'h': 'l',
    'J': 'm',
    'M': 'n',
    '#': 'o',
    '4': 'p',
    'q': 'q',
    '?': 'r',
    't': 's',
    'R': 't',
    'C': 'u',
    'x': 'v',
    'v': 'w',
    '{': 'x',
    'K': 'y',
    '1': 'z',
    '2': '1',
    'a': '2',
    '7': '3',
    'b': '4',
    '`': '5',
    '+': '6',
    '}': '7',
    '&': '8',
    '>': '9',
    ';': '0',
    '/': '@',
    'i': '#',
    '!': '$',
    ']': '_',
    '-': '&',
    'F': '-',
    '@': '+',
    'q': '(',
    'j': ')',
    'B': '/',
    'c': '*',
    'Y': '"',
    '^': ':',
    '$': ';',
    'O': '!',
    '5': '?',
    'E': '~',
    'I': '`',
    'l': '|',
    '%': '^',
    'u': '=',
    'g': '{',
    '0': '}',
    'S': '%',
    'N': '[',
    '9': ']',
    'p': '<',
    'r': '>',
    'd': '.',
    'w': ',',
    ' ': ' '
}
clear()
print("THANK YOU FOR INSTALLING BEASTCODE")
time.sleep(2)
print("THIS IS MY FIRTS PROGRAM")
time.sleep(2)
print("HOPE YOU ENJOY IT")
time.sleep(2)
print("-AUTHOR HyperBeasty")
time.sleep(2)
print("LAUNCHING BEASTCODE.....")
time.sleep(2)
while(True):
    clear()
    print("================================================")
    print("=        WELCOME TO BEASTCODE PROGRAM          =")
    print("================================================")
    print("THIS TOOL WILL ENCRYPT AND DECRYPT YOUR MESSAGE:")
    print("[1] ENCRYPT A MESSAGE")
    print("[2] DECRYPT A MESSAGE")
    print("[3] EXIT")

    option = (input("ENTER CHOICE HERE:"))
    if option == '1':
        while(True):
            clear()
            plain = input("ENTER THE NORMAL TEXT HERE: ")
            print('ENCRYPTING....')
            time.sleep(3)

            def encrypt(text):
                encryption = ''
                for letter in text:
                    if letter in beastcodeencrypt:
                        encryption = encryption + beastcodeencrypt[letter]
                    else:
                        print(
                            "INVALID CHARACTERS IDENTIFIED, PLEASE\nUSE NORMAL TEXT AND NUMBERS")
                return encryption
            print("ENCRYPTED TEXT: " + encrypt(plain))
            back = input("PRESS ENTER TO GO BACK TO MENU:")
            if back == '':
                break
            else:
                break

    elif option == '2':
        while(True):
            clear()
            plain = input("ENTER THE ENCRYPTED TEXT HERE: ")
            print("DECRYPTING....")
            time.sleep(3)

            def decrypt(text):
                decryption = ''
                for letter in text:
                    if letter in beastcodedecrypt:
                        decryption = decryption + beastcodedecrypt[letter]
                    else:
                        print(
                            "INVALID CHARACTERS OR ENCRYPTION \nENTER TEXT ENCRYPTED BY BEASTCODE")
                return decryption
            print("DECRYPTED TEXT: " + decrypt(plain))
            back = input("PRESS ENTER TO GO BACK TO MENU:")
            if back == '':
                break
            else:
                break

    elif option == '3':
        break

    else:
        print("ENTER A VALID OPTION")
        time.sleep(3)
