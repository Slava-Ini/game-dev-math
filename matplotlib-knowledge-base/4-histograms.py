import numpy as np
import matplotlib.pyplot as plt

# Normal distribution
ages = np.random.normal(20, 1.5, 1_000)

# `cumulative` - one way distribution
plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()], cumulative=True)
plt.show()
