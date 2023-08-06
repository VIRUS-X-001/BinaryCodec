from time import sleep
inf="""
 ____  _                         ____          _
| __ )(_)_ __   __ _ _ __ _   _ / ___|___   __| | ___  ___
|  _ \| | '_ \ / _` | '__| | | | |   / _ \ / _` |/ _ \/ __|
| |_) | | | | | (_| | |  | |_| | |__| (_) | (_| |  __/ (__
|____/|_|_| |_|\__,_|_|   \__, |\____\___/ \__,_|\___|\___|
                          |___/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
print("\033[2;32m"+inf)
def encode_text():
    sleep(1)
    text = input("Enter text to be encoded:- ")
    binary_code = ""
    sleep(2)
    for char in text:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_code += binary_char + " "

    print("Encoded binary code:", "\033[2;31m" + binary_code.strip())
    print("\033[2;32m"+"")
def decode_text():
    binary_string = input("Enter binary code to be decoded: ")
    sleep(3)
    binary_codes = binary_string.split()
    decoded_text = ""
    for code in binary_codes:
        decimal_value = int(code, 2)
        character = chr(decimal_value)
        decoded_text += character
        sleep(2)
    print("Decoded text:","\033[2;31m" + decoded_text)
    sleep(1)
def main():
    while True:
        print("\033[2;32m" +"")
        print("Select an option:\n1. Encode text\n2. Decode binary\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            encode_text()
        elif choice == "2":
            decode_text()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.\n")
if __name__ == "__main__":
    main()
