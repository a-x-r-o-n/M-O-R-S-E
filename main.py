from module import *

for i in msg.lower():
    if i ==" ":
        code = code + " " + "....."
    elif i in alphabets:
        code = code + " " + isAlphabet(i)

print(f"Morse code for the message {msg}: {code}")