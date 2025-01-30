import numpy as np
import matplotlib.pyplot as plt

thisDict = {
    "A" : 0,
    "B" : 0,
    "C" : 0,
    "D" : 0,
    "E" : 0,
    "F" : 0,
    "G" : 0,
    "H" : 0,
    "I" : 0,
    "J" : 0,
    "K" : 0,
    "L" : 0,
    "M" : 0,
    "N" : 0,
    "O" : 0,
    "P" : 0,
    "Q" : 0,
    "R" : 0,
    "S" : 0,
    "T" : 0,
    "U" : 0,
    "V" : 0,
    "W" : 0,
    "X" : 0,
    "Y" : 0,
    "Z" : 0
}

cipher = 'EGDHE TGXIN XHCDI LXIWD JIBPC NUTPG HPCSS XHIPH ITHPC SPSKT GHXIN XHCDI LXIWD JIRDB UDGIH PCSWD ETHMM'

counts = [0]*26
for l in cipher:
    for let in thisDict.keys():
        if let == l:
            thisDict[let] += 1

plt.bar(thisDict.keys(), thisDict.values())
plt.savefig('freq.png')