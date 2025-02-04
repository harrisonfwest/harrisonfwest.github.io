import numpy as np

def addCipher(cipher: str, shift: int) -> str:
    text = list(cipher)
    ct = []
    for t in text:
        if t == " ":
            ct.append(" ")
        else:
            ct.append(chr(((ord(t) - 97) + shift) % 26 + 97))
    return ''.join(ct)


def bruteForce(cipher: str) -> None:
    for i in np.arange(1, 26, 1):
        print(f'For {i} shift, plaintext said \"{addCipher(cipher, abs(i-26))}\". Decrypt by shifting an additional {abs(i-26)}')

def multCipher(cipher: str, shift: int) -> str:
    text = list(cipher)
    ct = []
    for t in text:
        if t == " ":
            ct.append(" ")
        else:
            ct.append(chr((((ord(t) - 97) * shift) % 26) + 97))
    return ''.join(ct)

def affineCipher(cipher: str, multShift: int, addShift: int):
    return (multCipher(addCipher(cipher, addShift), multShift))

def keywordCipher(cipher: str, keyword: str, keyLetter : str) -> str:
    # TODO: FINISH THIS FUNCTION
    codeDict = {
        1 : '',
        2 : '',
        3 : '',
        4 : '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: '',
        10: '',
        11: '',
        12: '',
        13: '',
        14: '',
        15: '',
        16: '',
        17: '',
        18: '',
        19: '',
        20: '',
        21: '',
        22: '',
        23: '',
        24: '',
        25: '',
        26: '',
    }
    used = []
    for t in keyword:
        if t in used:
            continue
        else:
            used.append(t)
        # now we have no duplicates in the keyword

    charNum = ord(t) - 96 # only subtract 96 because the dictionary is 1-indexed rather than 0-indexed as for mod math
    newUsed = []
    for t in used:
        codeDict[charNum] = t
        newUsed.append(t)
        if charNum + 1 > 26:
            charNum = charNum - 25
        else:
            charNum = charNum + 1
    # used[] is array of keyword w/o duplicates; newUsed is array of letters already inserted into alphabet key
    # charNum is the current


pt = ('when the government violates the peoples rights insurrection is for the people and for each portion of'
      ' the people the most sacred of the rights and the most indispensable of duties')
print(addCipher(pt, 16))
print(multCipher(pt, 16))
print(affineCipher(pt, 3, 24))

keywordDict = {
    ' ' : ' ',
    'a' : 'j',
    'b' : 'k',
    'c' : 'l',
    'd' : 'm',
    'e' : 'p',
    'f' : 'q',
    'g' : 'r',
    'h' : 'v',
    'i' : 'w',
    'j' : 'x',
    'k' : 'y',
    'l' : 'z',
    'm' : 'c',
    'n' : 'o',
    'o' : 'n',
    'p' : 's',
    'q' : 't',
    'r' : 'i',
    's' : 'u',
    't' : 'a',
    'u' : 'b',
    'v' : 'd',
    'w' : 'e',
    'x' : 'f',
    'y' : 'g',
    'z' : 'h',
}
answer = []
for t in pt:
    answer.append(keywordDict[t])
print (''.join(answer))