def decodeMorse(morse_code):
    MORSE_CODE = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
    }
    # convert space to l because if just use "split" every word will stick together
    lspace = morse_code.replace(" ", "l")
    # count the string with too much spacing
    count = lspace.count("lll")

    # if too much spacing make it to one space only
    if count >= 1:
        lspace = lspace.replace("lll", "ll")
    split_morse = lspace.split("l")

    for i, j in enumerate(split_morse):
        # notice that double "l" will create "" in the list so we convert that to a space
        if j == "":
            split_morse[i] = " "
        # convert the morse code to alphabets
        elif j in MORSE_CODE:
            split_morse[i] = MORSE_CODE[j]

    # return a sentence
    return "".join(split_morse).lstrip().rstrip()


x = '.... . -.--   .--- ..- -.. .'
print(decodeMorse(x))
