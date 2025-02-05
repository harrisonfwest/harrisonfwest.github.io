import numpy as np

def addCipher(cipher: str, shift: int) -> str:
    answer = ''
    for t in cipher:
        if t == ' ':
            answer += ' '
        else:
            num = ord(t) - 96 + shift
            while num > 26:
                num -= 26
            answer += chr(num + 96)
    return answer


def bruteForceAdd(cipher: str) -> None:
    for i in np.arange(1, 26, 1):
        print(f'For {i} shift, plaintext said \"{addCipher(cipher, abs(i-26))}\". Decrypt by shifting an additional {abs(i-26)}')

def multCipher(cipher: str, shift: int) -> str:
    answer = ''
    for t in cipher:
        if t == ' ':
            answer += ' '
        else:
            num = (ord(t) - 96) * shift
        while not (1 <= num <= 26):
            if num > 26:
                num -= 26
            elif num < 26:
                num += 26
        answer += chr(num + 96)
    return answer


def affineCipher(cipher: str, multShift: int, addShift: int) -> str:
    return (multCipher(addCipher(cipher, addShift), multShift))

def keywordCipher(cipher: str, keyword: str, keyLetter : str) -> str:
    codeAlph = {}
    alph = 'abcdefghijklmnopqrstuvwxyz'
    nodupe = ''
    for t in keyword:
        if not (t in nodupe):
            nodupe += t
    used = ''
    curr = ord(keyLetter) - 96
    for s in nodupe:
        codeAlph[curr] = s
        used += s
        if curr == 26:
            curr = 1
        else:
            curr += 1
    for v in alph:
        if not (v in used):
            codeAlph[curr] = v
            if curr == 26:
                curr = 1
            else:
                curr += 1
        used += v
    answer = ''
    for m in cipher:
        if m == ' ':
            answer += ' '
        else:
            answer += codeAlph[ord(m) - 96]
    return answer

pt = ('when the government violates the peoples rights insurrection is for the people and for each portion of'
      ' the people the most sacred of the rights and the most indispensable of duties')


ct = ('KCNQL HGKLS KCHFC LBNZL ARTFF HXGBN GKHFK LFCLZ JLPKC TKHKH FQLFF HYWNK LINDH QCNAT BNFFT XNNUN GZCNG '
          'KCNZL AIFKA PDKPA NHFGL KBTHG KTHGN IKCNB NKCLI PFNIK LQALI PDNKC NFPYF KHKPK HLGTW QCTYN KZTFK LDLBY '
          'HGNKC NTIIH KHLGF KNQPF NIHGT DTNFT ADHQC NAZHK CKCNB PWKHQ WHDTK HLGPF NIHGK CNFND LGIDL INJLP YALRN '
          'PFHGX KCNFN KZLBN KCLIF KLXNK CNAQA LIPDN FTBNK CLILS NGDAJ QKHLG RGLZG TFTGT SSHGN KATGF SLABT KHLGE')


def bruteForceAffine(cipher: str) -> None:
    for add in range(1, 25):
        for mult in [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
            print('mult decipher is ' + str(mult) + ', add decipher is ' + str(add) + ', message says ' + affineCipher(cipher, mult, add))


print(addCipher(pt, 16))
print(multCipher(pt, 17))
print(affineCipher(pt, 3, 24))
print(keywordCipher(pt, 'constitution', 'm'))



newCt = ''
for i in ct:
    if i != ' ':
        newCt += i.lower()
print(affineCipher(newCt, 21, 11))
