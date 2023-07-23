# Matplotlib 3D Plot Animation Lab

## Introduction

This lab will guide you on how to create a simple animation of a rotating 3D plot about all three axes using Matplotlib. We will use a sample dataset to create a basic wireframe, set axis labels, and rotate the axes.

## Steps

### Step 1: Import Libraries and Dataset

First, we need to import the necessary libraries and dataset. In this example, we will use the `matplotlib` and `mpl_toolkits.mplot3d` libraries to create the 3D plot, and the `axes3d.get_test_data()` function to generate a sample dataset.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Generate sample dataset
X, Y, Z = axes3d.get_test_data(0.05)
```

### Step 2: Create a 3D Plot

Next, we will create a 3D plot using the `plt.figure()` and `fig.add_subplot()` functions. We will also use the `ax.plot_wireframe()` function to plot the dataset as a wireframe.

```python
# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot wireframe
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```

### Step 3: Set Axis Labels

We will now set the axis labels for the 3D plot using the `ax.set_xlabel()`, `ax.set_ylabel()`, and `ax.set_zlabel()` functions.

```python
# Set axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
```

### Step 4: Rotate the Axes and Update the Plot

Finally, we will rotate the axes and update the plot using a for loop that cycles through a full rotation of elevation, then azimuth, roll, and all. We will use the `ax.view_init()` function to update the axis view and title, and the `plt.title()`, `plt.draw()`, and `plt.pause()` functions to display the animation.

```python
# Rotate the axes and update the plot
for angle in range(0, 360*4 + 1):
    # Normalize the angle to the range [-180, 180] for display
    angle_norm = (angle + 180) % 360 - 180

    # Cycle through a full rotation of elevation, then azimuth, roll, and all
    elev = azim = roll = 0
    if angle <= 360:
        elev = angle_norm
    elif angle <= 360*2:
        azim = angle_norm
    elif angle <= 360*3:
        roll = angle_norm
    else:
        elev = azim = roll = angle_norm

    # Update the axis view and title
    ax.view_init(elev, azim, roll)
    plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))

    # Display animation
    plt.draw()
    plt.pause(.001)
```

## Summary

In this lab, we learned how to create a simple animation of a rotating 3D plot about all three axes using Matplotlib. We used a sample dataset to create a basic wireframe, set axis labels, and rotated the axes. We also learned how to use the `ax.view_init()`, `plt.title()`, `plt.draw()`, and `plt.pause()` functions to update the plot and display the animation.
