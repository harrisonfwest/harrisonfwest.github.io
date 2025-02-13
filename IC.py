'''
num = 0
numList = [13, 2, 4, 26, 6, 17, 8, 10, 18, 4, 13, 12, 16, 15, 14, 6, 16, 16, 7, 11, 6, 12, 16, 12, 9, 11]
for val in numList:
    num += val**2
print(num)
'''

cipher = ('XPERG POEVO WIMPF EVOBE VODLS EWMQS MJQAF LBASI PAPQG OOPOR YPVVN PXOVL MWQEV OFUSK GHCZY TVOFA VIOLO FQBGY TDLEY HTDSO DUPIM OWZTZ QEJVX THOPA LYSWJ VXDLE OHOLK EFAPQ MGWYF ZYTVO BEXHG TFDWA ILXLW PQSZL PPJHC PXIEH OOXHC AUSIK GFXZV DYHTU SKGDF YIEFH OZXHG YTNLE OLCPX HOHZM IARVM JKRCW ITGSE OFXIL GATCI AFJIL TTGYU SVEGV GELIU IPZOT QMJYH OWAIZ ATQWS ZGEGK')
cipherText = ''
for char in cipher:
    if char != ' ':
        cipherText += char.lower()

cipher1 = ''
cipher2 = ''
cipher3 = ''

for i in range(0, len(cipherText)):
    if i % 3 == 0:
        cipher1 += cipherText[i]
    elif i % 3 == 1:
        cipher2 += cipherText[i]
    elif i % 3 == 2:
        cipher3 += cipherText[i]



'''
from frequency_analysis import freqFinder
freqFinder(cipher1, 'newOne')
freqFinder(cipher2, 'newTwo')
freqFinder(cipher3, 'newThree')
'''


from simple_ciphers import addCipher

newCipher1 = ''
newCipher2 = ''
newCipher3 = ''

first = [16, 11]
second = [24, 5, 15]
third = [23, 19, 9, 4, 22, 12, 6]

for a in first:
    for b in second:
        for c in third:
            newCipher1 = addCipher(cipher1, a)
            newCipher2 = addCipher(cipher2, b)
            newCipher3 = addCipher(cipher3, c)
            finalText = ''
            for i in range(0, 100):
                finalText = finalText + newCipher1[i] + newCipher2[i] + newCipher3[i]
            print(finalText)