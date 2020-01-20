englishInput = input("Enter an English phrase to be translated into Morse Code: ")
inputArray = []
morseCode = []

for letter in englishInput: 
    inputArray.append(letter)

for character in inputArray:
    if character.lower() == "a":
        morseCode.append(".-")
    elif character.lower() == "b":
        morseCode.append("-...")
    elif character.lower() == "c":
        morseCode.append("-.-.")
    elif character.lower() == "d":
        morseCode.append("-..")
    elif character.lower() == "e":
        morseCode.append(".")
    elif character.lower() == "f":
        morseCode.append("..-.")
    elif character.lower() == "g":
        morseCode.append("--.")
    elif character.lower() == "h":
        morseCode.append("....")
    elif character.lower() == "i":
        morseCode.append("..")
    elif character.lower() == "j":
        morseCode.append(".---")
    elif character.lower() == "k":
        morseCode.append("-.-")
    elif character.lower() == "l":
        morseCode.append(".-..")
    elif character.lower() == "m":
        morseCode.append("--")
    elif character.lower() == "n":
        morseCode.append("-.")
    elif character.lower() == "o":
        morseCode.append("---")
    elif character.lower() == "p":
        morseCode.append(".--.")
    elif character.lower() == "q":
        morseCode.append("--.-")
    elif character.lower() == "r":
        morseCode.append(".-.")
    elif character.lower() == "s":
        morseCode.append("...")
    elif character.lower() == "t":
        morseCode.append("-")
    elif character.lower() == "u":
        morseCode.append("..-")
    elif character.lower() == "v":
        morseCode.append("...-")
    elif character.lower() == "w":
        morseCode.append(".--")
    elif character.lower() == "x":
        morseCode.append("-..-")
    elif character.lower() == "y":
        morseCode.append("-.--")
    elif character.lower() == "z":
        morseCode.append("--..")
    elif character.lower() == "1":
        morseCode.append(".----")
    elif character.lower() == "2":
        morseCode.append("..---")
    elif character.lower() == "3":
        morseCode.append("...--")
    elif character.lower() == "4":
        morseCode.append("....-")
    elif character.lower() == "5":
        morseCode.append(".....")
    elif character.lower() == "6":
        morseCode.append("-....")
    elif character.lower() == "7":
        morseCode.append("--...")
    elif character.lower() == "8":
        morseCode.append("---..")
    elif character.lower() == "9":
        morseCode.append("----.")
    elif character.lower() == "0":
        morseCode.append("-----")
    elif character.lower() == " ":
        #In morse code,spaces are represented by seven dot spaces. 
        morseCode.append("       ")
    elif character.lower() == ",":
        morseCode.append("--..--")
    elif character.lower() == ".":
        morseCode.append(".-.-.-")
    elif character.lower() == "?":
        morseCode.append("..--..")
    elif character.lower() == ";":
        morseCode.append("-.-.-.")
    elif character.lower() == ":":
        morseCode.append("---...")
    elif character.lower() == "/":
        morseCode.append("-..-.")
    elif character.lower() == "-":
        morseCode.append("-....-")
    elif character.lower() == "'":
        morseCode.append(".----.")
    elif character.lower() == "_":
        morseCode.append("..--.-")
    elif character.lower() == "(":
        morseCode.append("-.--.")
    elif character.lower() == ")":
        morseCode.append("-.--.-")
    elif character.lower() == "+":
        morseCode.append(".-.-.")
    elif character.lower() == "@":
        morseCode.append(".--.-.")
    else: 
        print("Whoops! Unknown character cannot be represented by morse code!")

def arraytoString(s):
    finalString = " "
    return (finalString.join(s))

finalMorseCode = arraytoString(morseCode)
print(finalMorseCode)
