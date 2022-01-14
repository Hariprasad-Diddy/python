symbols = {
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": ".-",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}

# Users entered word to convert  into Mors Code
word = input("Enter words to convert into MORS Code : ")
def mors_code_convertor(word):
    mors_code = ""
    for l in range(len(word)):
        # Checking the user enterd each character is available in Symbols Dictionary
        # If Character is available then it is converting
        if word[l].lower() in symbols.keys():
            mors_code = mors_code+""+symbols.get(word[l].lower())
        
        # Checking if the user enterd string contains spaces or not
        # If spaces is available then adding that space in mors code
        elif word[l] == " ":
            mors_code = mors_code + " "
    print(f'Converted Mors Code was : "{mors_code}"')
mors_code_convertor(word)
