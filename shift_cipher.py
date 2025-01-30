import numpy as np

def shifter(cipher: str, shift: int):
    text = list(cipher)
    ct = []
    for t in text:
        if t == " ":
            ct.append(" ")
        elif ord(t) + shift > 122:
            ct.append(chr(ord(t) + shift - 26))
        else:
            ct.append(chr(ord(t) + shift))
    return ''.join(ct)


def bruteForce(cipher: str):
    for i in np.arange(1, 26, 1):
        print(f'For {i} shift, plaintext said \"{shifter(cipher, abs(i-26))}\". Decrypt by shifting an additional {abs(i-26)}')

def main():
    while True:
        inp = input('Enter a lowercase string to shift (can include spaces), followed by a comma and the number'
                    ' by which to shift. Or, enter 0 to quit: ')
        if inp == "0":
            break
        else:
            print(shifter(inp.split(',')[0], int(inp.split(',')[1])))

bruteForce('ziffiqsiolvfcmm')