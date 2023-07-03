# Python Matplotlib Step-by-Step Lab

## Multiple Axes Animation

### Introduction

This step-by-step lab demonstrates how to create an animation with multiple subplots using Matplotlib in Python. The example shows how to animate a circle and a sine curve across two different subplots.

### Steps

#### Import Libraries

The first step is to import the required libraries, including Matplotlib, NumPy, and Matplotlib's animation module.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.patches import ConnectionPatch
```

#### Create the Figure and Subplots

The second step is to create the figure and subplots that will be used for the animation. In this example, we create two subplots side-by-side with different aspect ratios. The left subplot is a unit circle, and the right subplot is an empty plot that will be used to animate a sine curve.

```python
fig, (axl, axr) = plt.subplots(
    ncols=2,
    sharey=True,
    figsize=(6, 2),
    gridspec_kw=dict(width_ratios=[1, 3], wspace=0),
)
axl.set_aspect(1)
axr.set_box_aspect(1 / 3)
axr.yaxis.set_visible(False)
axr.xaxis.set_ticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
```

#### Draw the Circle and Initial Point

The third step is to draw the circle and initial point on the left subplot. We create an array of angles to generate the circle, and then plot the sine and cosine of each angle. We also plot a single point at the origin.

```python
x = np.linspace(0, 2 * np.pi, 50)
axl.plot(np.cos(x), np.sin(x), "k", lw=0.3)
point, = axl.plot(0, 0, "o")
```

#### Draw the Sine Curve

The fourth step is to draw the sine curve on the right subplot. We create an array of angles, and then plot the sine of each angle. We also save the `sine` plot object, which we will update later in the animation.

```python
sine, = axr.plot(x, np.sin(x))
```

#### Draw the Connection Line

The fifth step is to draw a dotted line connecting the two subplots. We create a `ConnectionPatch` object that connects the origin of the left subplot to the right edge of the right subplot. We also save the `con` patch object, which we will update later in the animation.

```python
con = ConnectionPatch(
    (1, 0),
    (0, 0),
    "data",
    "data",
    axesA=axl,
    axesB=axr,
    color="C0",
    ls="dotted",
)
fig.add_artist(con)
```

#### Define the Animation Function

The sixth step is to define the animation function. This function will be called for each frame of the animation, and will update the position of the point on the left subplot, the position and data of the sine curve on the right subplot, and the position of the connection patch.

```python
def animate(i):
    x = np.linspace(0, i, int(i * 25 / np.pi))
    sine.set_data(x, np.sin(x))
    x, y = np.cos(i), np.sin(i)
    point.set_data([x], [y])
    con.xy1 = x, y
    con.xy2 = i, y
    return point, sine, con
```

#### Create the Animation

The seventh step is to create the animation object using the `FuncAnimation` function. We pass in the figure object, the animation function, the interval between frames in milliseconds, the number of frames, and a delay before repeating the animation.

```python
ani = animation.FuncAnimation(
    fig,
    animate,
    interval=50,
    blit=False,  # blitting can't be used with Figure artists
    frames=x,
    repeat_delay=100,
)
```

#### Show the Animation

The final step is to show the animation using the `show` function of the `pyplot` module.

```python
plt.show()
```

### Summary

This step-by-step lab demonstrated how to create an animation with multiple subplots using Matplotlib in Python. The example showed how to animate a circle and a sine curve across two different subplots. The steps included importing libraries, creating the figure and subplots, drawing the circle and initial point, drawing the sine curve, drawing the connection line, defining the animation function, creating the animation object, and showing the animation.
