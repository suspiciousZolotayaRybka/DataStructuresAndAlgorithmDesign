import numpy as np
import matplotlib.pyplot as plt

sims: int = 1000000

A = np.random.uniform(1, 5, sims)
B = np.random.uniform(2, 6, sims)

duration: int = A + B

plt.figure(figsize = (3, 1.5))
plt.hist(duration, density = True)
plt.axvline(9, color = 'r')
plt.show()
print((duration > 9).sum()/sims)