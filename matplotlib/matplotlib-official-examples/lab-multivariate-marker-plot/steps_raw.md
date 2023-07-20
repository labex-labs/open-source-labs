# Mapping Marker Properties to Multivariate Data

## Introduction

In this lab, you will learn how to use different properties of markers to plot multivariate datasets using Python's Matplotlib library. Specifically, you will learn how to represent a successful baseball throw as a smiley face with marker size mapped to the skill of thrower, marker rotation to the take-off angle, and thrust to the marker color.

## Steps

### Step 1: Import Libraries

In this step, you will import the necessary libraries for this lab. Specifically, you will import `Matplotlib`, `Numpy`, and various modules from `Matplotlib` such as `MarkerStyle`, `TextPath`, and `Affine2D`.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import Normalize
from matplotlib.markers import MarkerStyle
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
```

### Step 2: Define Success Symbols

In this step, you will define the three success symbols that will be used to represent the success of a baseball throw. Specifically, you will define a smiley face for a successful throw, a neutral face for a partially successful throw, and a sad face for an unsuccessful throw.

```python
SUCCESS_SYMBOLS = [
    TextPath((0, 0), "☹"),
    TextPath((0, 0), "😒"),
    TextPath((0, 0), "☺"),
]
```

### Step 3: Generate Random Data

In this step, you will generate random data for the skill of the thrower, take-off angle, thrust, success, and position. Specifically, you will generate 25 data points for each variable, except for position, which will have 2 coordinates for each data point.

```python
N = 25
np.random.seed(42)
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
takeoff_angles = np.random.normal(0, 90, N)
thrusts = np.random.uniform(size=N)
successful = np.random.randint(0, 3, size=N)
positions = np.random.normal(size=(N, 2)) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)
```

### Step 4: Define Color Map

In this step, you will define the color map that will be used to map the thrust of the throw to the color of the marker. Specifically, you will use the "plasma" color map from Matplotlib.

```python
cmap = plt.colormaps["plasma"]
```

### Step 5: Create Plot

In this step, you will create the plot using the random data generated earlier. Specifically, you will plot each data point as a marker with the success symbol determined by the success variable, the size determined by the skill variable, the rotation determined by the take-off angle variable, and the color determined by the thrust variable.

```python
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")
```

### Step 6: Display Plot

In this step, you will display the plot using Matplotlib's `show()` function.

```python
plt.show()
```

## Summary

In this lab, you learned how to use different properties of markers to plot multivariate datasets using Python's Matplotlib library. Specifically, you learned how to represent a successful baseball throw as a smiley face with marker size mapped to the skill of thrower, marker rotation to the take-off angle, and thrust to the marker color. By following the steps outlined in this lab, you can create similar plots for your own multivariate datasets.
