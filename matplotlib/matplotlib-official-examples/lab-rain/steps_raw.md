# Python Matplotlib Rain Simulation

## Introduction

This lab is a step-by-step tutorial on how to create a rain simulation using Python's Matplotlib library. The simulation will animate the scale and opacity of 50 scatter points to simulate raindrops falling on a surface.

## Steps

### Step 1: Create a new Figure and Axes

The first step is to create a new figure and an axes which fills it. This will be the canvas on which the simulation will be drawn.

```python
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
```

### Step 2: Create Rain Data

Next, we will create the rain data. We will create 50 raindrops in random positions, with random growth rates, and random colors.

```python
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, (2,)),
                                      ('size',     float),
                                      ('growth',   float),
                                      ('color',    float, (4,))])

rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)
```

### Step 3: Construct the Scatter Plot

Now, we will construct the scatter plot which we will update during the animation as the raindrops develop.

```python
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')
```

### Step 4: Create the Update Function

The update function will be called by the FuncAnimation object to update the scatter plot during the animation.

```python
def update(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % n_drops

    # Make all colors more transparent as time progresses.
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # Make all circles bigger.
    rain_drops['size'] += rain_drops['growth']

    # Pick a new position for oldest rain drop, resetting its size,
    # color and growth factor.
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    rain_drops['size'][current_index] = 5
    rain_drops['color'][current_index] = (0, 0, 0, 1)
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
```

### Step 5: Create the Animation

Finally, we will create the animation using the FuncAnimation object, passing in the figure, the update function, the interval between frames in milliseconds, and the number of frames to save.

```python
animation = FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```

## Summary

In this lab, we learned how to create a rain simulation using Python's Matplotlib library. We created a new Figure and Axes, created the rain data, constructed the scatter plot, created the update function, and created the animation using the FuncAnimation object.
