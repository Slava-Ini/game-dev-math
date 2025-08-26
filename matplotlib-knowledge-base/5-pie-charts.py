import numpy as np
import matplotlib.pyplot as plt


langs = ["Python", "C++", "Java", "C#", "Go"]
votes = [50, 24, 14, 6, 17]
explodes = [0, 0, 0, 0.2, 0]

# `explode` is a part of a pie chart that sticks out
# `autopct` show formatted % numbers
# `pctdistance` distance of % from the center
plt.pie(votes, labels=langs, explode=explodes,
        autopct="%.2f%%", pctdistance=1.3, startangle=90)
plt.show()
