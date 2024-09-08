alphabets = [chr(i) for i in range(97,123)]
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
# -------------------------------------------------------
def morseToPlain(traverse):
    if traverse == ".....":
        return " "
    elif traverse == "._":
        return 'a'
    elif traverse == "_...":
        return 'b'
    elif traverse == "_._.":
        return 'c'
    elif traverse == "_..":
        return 'd'
    elif traverse == ".":
        return 'e'
    elif traverse == ".._.":
        return 'f'
    elif traverse == "__.":
        return 'g'
    elif traverse == "....":
        return 'h'
    elif traverse == "..":
        return 'i'
    elif traverse == ".___":
        return 'j'
    elif traverse == "_._":
        return 'k'
    elif traverse == "._..":
        return 'l'
    elif traverse == "__":
        return 'm'
    elif traverse == "_.":
        return 'n'
    elif traverse == "___":
        return 'o'
    elif traverse == ".__.":
        return 'p'
    elif traverse == "__._":
        return 'q'
    elif traverse == "._.":
        return 'r'
    elif traverse == "...":
        return 's'
    elif traverse == "_":
        return 't'
    elif traverse == ".._":
        return 'u'
    elif traverse == "..._":
        return 'v'
    elif traverse == ".__":
        return 'w'
    elif traverse == "_.._":
        return 'x'
    elif traverse == "_.__":
        return 'y'
    elif traverse == "__..":
        return 'z'
def plainText(*code):
    msg = ""
    for traverse in code:
        for i in traverse:
            msg = msg + morseToPlain(i)
    #print(f"Message: {msg}")
    return msg