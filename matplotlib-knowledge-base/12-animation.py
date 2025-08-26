import numpy as np
import matplotlib.pyplot as plt
import random

heads_tails = [0, 0]

for _ in range(100_000):
    heads_tails[random.randint(0, 1)] += 1
    plt.bar(["Heads", "Tails"], heads_tails, color=["red", "blue"])
    # - Basically pauses before showing it again
    plt.pause(0.001)

plt.show()

