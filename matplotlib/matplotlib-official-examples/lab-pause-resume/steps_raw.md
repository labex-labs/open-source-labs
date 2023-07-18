# Matplotlib Animation Lab

## Introduction

In this lab, you will learn how to create an animation with Matplotlib. Specifically, you will learn how to pause and resume an animation using the `Animation.pause()` and `Animation.resume()` methods.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries to create an animation with Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
```

### Step 2: Define the Animation

In this step, we will define the animation that we want to create. We will create an animation that displays a normal distribution that moves to the right with each frame.

```python
class PauseAnimation:
    def __init__(self):
        # Create the figure and axis
        fig, ax = plt.subplots()
        ax.set_title('Click to pause/resume the animation')

        # Create the x-axis values
        x = np.linspace(-0.1, 0.1, 1000)

        # Start with a normal distribution
        self.n0 = (1.0 / ((4 * np.pi * 2e-4 * 0.1) ** 0.5)
                   * np.exp(-x ** 2 / (4 * 2e-4 * 0.1)))

        # Create the plot
        self.p, = ax.plot(x, self.n0)

        # Create the animation
        self.animation = animation.FuncAnimation(
            fig, self.update, frames=200, interval=50, blit=True)

        # Set the animation as unpaused
        self.paused = False

        # Add a button press event to toggle pause
        fig.canvas.mpl_connect('button_press_event', self.toggle_pause)

    def toggle_pause(self, *args, **kwargs):
        # Toggle between paused and unpaused
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, i):
        # Update the normal distribution
        self.n0 += i / 100 % 5
        self.p.set_ydata(self.n0 % 20)
        return (self.p,)
```

### Step 3: Create the Animation Object

In this step, we will create an object of the `PauseAnimation` class that we defined in step 2.

```python
pa = PauseAnimation()
```

### Step 4: Show the Animation

In this step, we will show the animation that we created in step 2.

```python
plt.show()
```

## Summary

In this lab, you learned how to create an animation with Matplotlib and how to pause and resume the animation using the `Animation.pause()` and `Animation.resume()` methods. You also learned how to create an interactive animation that responds to user input. With this knowledge, you can create your own custom animations and add interactivity to them.
