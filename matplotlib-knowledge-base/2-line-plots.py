import numpy as np
import matplotlib.pyplot as plt

# Generate yers
years = [2006 + x for x in range(16)]
weights = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80,
          82, 82, 83, 81, 80, 83]

# `lw` - line width
plt.plot(years, weights, c="b", lw=3, linestyle="--")
# - Similarly this can be done using positional parameters
# plt.plot(years, weights, "b--", lw=3)
plt.show()
