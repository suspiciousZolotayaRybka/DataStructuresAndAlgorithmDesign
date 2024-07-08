import random
import numpy as np
import matplotlib.pyplot as plt


# Define the ship sizes
ships = {"Aircraft Carrier": 5, "Battleship": 4, "Submarine": 3, "Destroyer": 3, "Patrol Boat": 2}

# Run the Monte Carlo simulation for battleship# Monte Carlo equivalent
num_ship_spaces: int = sum(size for ship, size in ships.items())
print(num_ship_spaces)
num_spaces: int = 100

sims: int = 1000000
avg_hits: int = np.random.uniform(num_ship_spaces, num_spaces, sims)

plt.figure(figsize=(20, 10))
plt.hist(avg_hits, bins=50, density = True, alpha=0.75)
plt.xlabel('Number of Shots')
plt.ylabel('Density')
plt.title('Histogram of Shots to Sink All Ships')
plt.show()