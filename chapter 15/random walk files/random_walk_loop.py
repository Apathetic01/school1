import matplotlib.pyplot as plt
from random import choice
import time  # Import the time module for delaying between walks

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=500):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

# Continuously generate and display random walks.
while True:
    # Create a RandomWalk instance.
    rw = RandomWalk(5_00)
    rw.fill_walk()

    # Plotting the Random Walk
    plt.style.use('classic')
    fig, ax = plt.subplots()

    # Plot the points in the walk.
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolor='green', s=10)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='red', s=10)

   

    # Display the plot.
    plt.show()

    # Delay for a moment before generating the next walk.
    time.sleep(2)  # Sleep for 2 seconds between walks
