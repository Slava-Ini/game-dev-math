import numpy as np
import matplotlib.pyplot as plt

# - Option 1
# heights = np.random.normal(172, 8, 300)

# plt.boxplot(heights)

# - Option 2
first = np.linspace(0, 10, 25)
second = np.linspace(10, 200, 25)
third = np.linspace(200, 210, 25)
fourth = np.linspace(210, 230, 25)

data = np.concatenate((first, second, third, fourth))

plt.boxplot(data)
plt.show()
