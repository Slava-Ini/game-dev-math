import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(1_000) * 100
y_data = np.random.random(1_000) * 100

# `c/color` - hex, string color
# `marker` - the sign of a plotted point
# `s/size` - size
# `alpha` - alpha channel
plt.scatter(x_data, y_data, c="#00f", marker="*", s=100, alpha=0.3)
plt.show()
