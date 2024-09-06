def isAlphabet(a):
    if a == 'a':
        return "._"
    elif a == 'b':
        return "_..."
    elif a == 'c':
        return "_._."
    elif a == 'd':
        return "_.."
    elif a == 'e':
        return "."
    elif a == 'f':
        return ".._."
    elif a == 'g':
        return "__."
    elif a == 'h':
        return "...."
    elif a == 'i':
        return ".."
    elif a == 'j':
        return ".___"
    elif a == 'k':
        return "_._"
    elif a == 'l':
        return "._.."
    elif a == 'm':
        return "__"
    elif a == 'n':
        return "_."
    elif a == 'o':
        return "___"
    elif a == 'p':
        return ".__."
    elif a == 'q':
        return "__._"
    elif a == 'r':
        return "._."
    elif a == 's':
        return "..."
    elif a == 't':
        return "_"
    elif a == 'u':
        return ".._"
    elif a == 'v':
        return "..._"
    elif a == 'w':
        return ".__"
    elif a == 'x':
        return "_.._"
    elif a == 'y':
        return "_.__"
    elif a == 'z':
        return "__.."
    

msg = input("Enter your message: ")
code = ""
alphabets = [chr(i) for i in range(97,123)]