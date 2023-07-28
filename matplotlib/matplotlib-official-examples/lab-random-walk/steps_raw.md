# Animated 3D Random Walk in Matplotlib

## Introduction

In this lab, we will learn how to create an animated 3D random walk plot using Matplotlib library in Python. We will create a 3D plot and simulate a random walk with 40 particles that move randomly in 3D space.

## Steps

### Step 1: Import Required Libraries

We begin by importing the required libraries. We will use `numpy` to generate random numbers and `matplotlib` to create the plot.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
```

### Step 2: Define Random Walk Function

We define a function that generates a random walk with a given number of steps and maximum step size. The function takes two inputs: `num_steps` is the total number of steps in the random walk and `max_step` is the maximum size of each step. We use `numpy.random` to generate random numbers for the steps and `numpy.cumsum` to compute the cumulative sum of the steps to obtain the final position.

```python
def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk
```

### Step 3: Define Update Function

We define a function that updates the plot for each frame of the animation. The function takes three inputs: `num` is the current frame number, `walks` is a list of all the random walks, and `lines` is a list of all the lines in the plot. For each line and walk, we update the data for the x, y, and z coordinates of the line up to the current frame number. We use `line.set_data()` and `line.set_3d_properties()` to update the x-y and z coordinates, respectively.

```python
def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines
```

### Step 4: Generate Random Walks

We generate 40 random walks with 30 steps each using the `random_walk()` function defined earlier. We store all the random walks in a list called `walks`.

```python
# Data: 40 random walks as (num_steps, 3) arrays
num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]
```

### Step 5: Create 3D Plot

We create a 3D plot using `matplotlib`. We add an empty line for each random walk to the plot. We set the limits for the x, y, and z axes to be between 0 and 1.

```python
# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Create lines initially without data
lines = [ax.plot([], [], [])[0] for _ in walks]

# Setting the axes properties
ax.set(xlim3d=(0, 1), xlabel='X')
ax.set(ylim3d=(0, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')
```

### Step 6: Create Animation

We create an animation using the `FuncAnimation` class from `matplotlib.animation`. We pass the figure object, the update function, the total number of frames (which is equal to the number of steps in the random walks), the list of all random walks, and the list of all lines as arguments to the `FuncAnimation` constructor.

```python
# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
```

### Step 7: Display Animation

Finally, we display the animation using `plt.show()`.

```python
plt.show()
```

## Summary

We have learned how to create an animated 3D random walk plot using Matplotlib library in Python. We generated random walks and updated the plot for each frame of the animation. This technique can be used for visualizing particle movement, diffusion, and other stochastic processes in 3D space.
