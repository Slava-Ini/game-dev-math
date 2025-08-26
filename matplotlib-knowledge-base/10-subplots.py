import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sine Wave")

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title("Cosine Wave")

axs[1, 0].plot(x, np.random.random(100))
axs[1, 0].set_title("Random Function")

axs[1, 1].plot(x, np.log(x))
axs[1, 1].set_title("Log Wave")
axs[1, 1].set_xlabel("TEST")

plt.show()

# - Export (save) plots
# plt.savefig("plots.png", dpi=300, transparent=False, pad_inches=20.2)
