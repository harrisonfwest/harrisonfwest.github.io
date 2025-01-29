def encrypter():
    plaintext = list(input('Enter a string of text to be shifted (only alphabetical characters, spaces allowed): '))
    shift = int(input("Enter a shift value: "))
    ciphertext = []
    for ptChar in plaintext:
        if ptChar == " ":
            ciphertext.append(" ")
        elif ord(ptChar) + shift > 122:
            ciphertext.append(chr(ord(ptChar) + shift - 26))
        else:
            ciphertext.append(chr(ord(ptChar) + shift))
    result = ''.join(ciphertext)
    print('The shifted code is: ' + result)

def decrypter(cipher: str, shift: int):
    text = list(cipher)
    ct = []
    for t in text:
        if t == " ":
            ct.append(" ")
        elif ord(t) - shift < 97:
            ct.append(chr(ord(t) - shift + 26))
        else:
            ct.append(chr(ord(t) - shift))
    return ''.join(ct)



def bruteForce(cipher: str):
    for i in range(26):
        print('For shift of ' + str(i) + ' characters, code said \"' + decrypter(cipher, i) + "\"")


bruteForce("mbfx yebxl ebdx tg tkkhp")