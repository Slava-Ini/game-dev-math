import numpy as np
import matplotlib.pyplot as plt

x = ["C++", "C#", "Python", "Java", "Go"]
y = [20, 50, 140, 1, 45]

# `align` - the start of bar chart
plt.bar(x, y, color="r", align="edge", width=0.5,
        edgecolor="green", lw=5)
plt.show()
