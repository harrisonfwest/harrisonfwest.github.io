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
    codeDict = {}
    for i in range(1, 26):
        codeDict[i] = ''
    alph = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    used = []
    charNum = ord(keyLetter) - 96 # starting index in dictionary (of key letter)
    for t in keyword:
        if t in used or t == " ":
            continue
        else:
            codeDict[charNum] = t
            if charNum == 26:
                charNum = 1
            else:
                charNum += 1
            used.append(t)
    for t in alph:
        if t in used:
            continue
        else:
            codeDict[charNum] = t
            if charNum == 26:
                charNum = 1
            else:
                charNum += 1
        used.append(t)
    answer = []
    for t in cipher:
        if t == " ":
            answer.append(" ")
        else:
            answer.append(codeDict[ord(str(t)) - 96])
    return(''.join(answer))

def hw3q4():
    pt = ('when the government violates the peoples rights insurrection is for the people and for each portion of'
      ' the people the most sacred of the rights and the most indispensable of duties')
    print(addCipher(pt, 16))
    print(multCipher(pt, 16))
    print(affineCipher(pt, 3, 24))
    print(keywordCipher(pt, 'constitution', 'm'))

def hw3q5():
    ct = ('KCNQL HGKLS KCHFC LBNZL ARTFF HXGBN GKHFK LFCLZ JLPKC TKHKH FQLFF HYWNK LINDH QCNAT BNFFT XNNUN GZCNG '
          'KCNZL AIFKA PDKPA NHFGL KBTHG KTHGN IKCNB NKCLI PFNIK LQALI PDNKC NFPYF KHKPK HLGTW QCTYN KZTFK LDLBY '
          'HGNKC NTIIH KHLGF KNQPF NIHGT DTNFT ADHQC NAZHK CKCNB PWKHQ WHDTK HLGPF NIHGK CNFND LGIDL INJLP YALRN '
          'PFHGX KCNFN KZLBN KCLIF KLXNK CNAQA LIPDN FTBNK CLILS NGDAJ QKHLG RGLZG TFTGT SSHGN KATGF SLABT KHLGE')
    newCt = []
    for t in ct:
        if t.isalpha() and t != " ":
            newCt.append(t.lower())
    bruteForce(''.join(newCt)) # not a simple additive shift

ct = ('KCNQL HGKLS KCHFC LBNZL ARTFF HXGBN GKHFK LFCLZ JLPKC TKHKH FQLFF HYWNK LINDH QCNAT BNFFT XNNUN GZCNG '
          'KCNZL AIFKA PDKPA NHFGL KBTHG KTHGN IKCNB NKCLI PFNIK LQALI PDNKC NFPYF KHKPK HLGTW QCTYN KZTFK LDLBY '
          'HGNKC NTIIH KHLGF KNQPF NIHGT DTNFT ADHQC NAZHK CKCNB PWKHQ WHDTK HLGPF NIHGK CNFND LGIDL INJLP YALRN '
          'PFHGX KCNFN KZLBN KCLIF KLXNK CNAQA LIPDN FTBNK CLILS NGDAJ QKHLG RGLZG TFTGT SSHGN KATGF SLABT KHLGE')
newCt = []
for t in ct:
    if t.isalpha() and t != " ":
        newCt.append(t.lower())
def affineBruteForce(cipher: str) -> None:
    for add in range(1, 25):
        for mult in [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
            print('mult decipher is ' + str(mult) + ', add decipher is ' + str(add) + ', message says ' + affineCipher(cipher, mult, add))

print(addCipher(multCipher(''.join(newCt), 5), 3))