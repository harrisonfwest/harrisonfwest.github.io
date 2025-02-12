import numpy as np
import matplotlib.pyplot as plt

# testCipher = 'EGDHE TGXIN XHCDI LXIWD JIBPC NUTPG HPCSS XHIPH ITHPC SPSKT GHXIN XHCDI LXIWD JIRDB UDGIH PCSWD ETHMM'

def freqFinder(cipher: str, fileName:str):
    thisDict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for l in cipher:
        for let in thisDict.keys():
            if let == l:
                thisDict[let] += 1
    plt.bar(thisDict.keys(), thisDict.values())
    plt.savefig(fileName + '.png')