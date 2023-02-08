from random import seed, randrange, randint, random
import matplotlib.pyplot as plt
import sys

# 1

seed(1)
series = [randint(100, 500) for i in range(100)]
plt.plot(series)
plt.show()

# 2

seed(2)
series = [randrange(1000) for i in range(100)]
plt.plot(series)
plt.show()

# 3

seed(sys.argv[1])
random_walk = list()
random_walk.append(-1 if random() < 0.5 else 1)
l = int(sys.argv[2])

for i in range(1, l):
    movement = -1 if random() < 0.5 else 1
    value = random_walk[i-1] + movement
    random_walk.append(value)
plt.plot(random_walk)
plt.show()