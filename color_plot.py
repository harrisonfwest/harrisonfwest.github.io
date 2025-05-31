# Color-space plotting

import numpy as np
import matplotlib.pyplot as plt

reds = np.arange(0, 1, 1/100)
greens = np.arange(0, 1, 1/100)
blues = np.arange(0, 1, 1/256)

for r in reds:
    for g in greens:
        plt.scatter(r, g, color=(r, g, 0), s=2)
plt.show()