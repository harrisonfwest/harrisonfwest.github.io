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
    for i in range(26):
        print('For shift of ' + str((i + 25) % 26) + ' characters, code said \"' + shifter(cipher, (i + 25) % 26) + "\"")

# bruteForce("mbfx yebxl ebdx tg tkkhp")

print(shifter("modular arithmetic and spreadsheets", 10))