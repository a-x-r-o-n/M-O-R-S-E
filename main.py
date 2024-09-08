from module import *
def plainToMorse(msg):
    code = ""
    for i in msg.lower():
        if i ==" ":
            code = code + " " + "....."
        elif i in alphabets:
            code = code + " " + isAlphabet(i)
    print(f"Morse code for the message {msg}: {code}")
def morseToPlain(Mmessage):
    print(f"Message: {plainText(Mmessage.split(' '))}")
def main():
    menu = input("1) Plain to Morse\t(or)\tMors to Plain\nenter choice either 1 or 2: ")
    if menu == '1':
        plainToMorse(input("Enter your message: "))
    elif menu == '2':
        morseToPlain(input("Enter Morse: "))
if __name__ == '__main__':
    main()