import matplotlib.pyplot as plt


def fun1(x):
    return 10 * x


def fun2(x):
    return 5 * x + 20


MAX_X = 100
x = range(MAX_X)

y1, y2 = zip(*[(fun1(val), fun2(val)) for val in x])

plt.plot(x, y1)
plt.plot(x, y2)
plt.ylabel("some numbers")
plt.show()
