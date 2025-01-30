import numpy as np
import matplotlib.pyplot as plt

cipher = ("EGDHE TGXIN XHCDI LXIWD JIBPC NUTPG HPCSS XHIPH ITHPC SPSKT GHXIN XHCDI LXIWD JIRDB UDGIH PCSWD ETHMM")
alph = ('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z').split()
counts = [0]*26
for l in cipher:
    for let in alph:
        if let == l:
            counts[ord(let) - ord('A')] += 1
