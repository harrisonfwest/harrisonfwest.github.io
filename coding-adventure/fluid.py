import matplotlib.pyplot as plt
import numpy as np

class particle():
    def __init__(self, m : float, r : float):
        self.mass = m
        self.size = r
class pool():
    def __init__(self, num_drops : int, w : float, d : float, h : float):
        self.drop_count = num_drops
        self.width = w
        self.depth = d
        self.height = h
        self.volume = w * d * h
        for _ in range(self.drop_count):
            