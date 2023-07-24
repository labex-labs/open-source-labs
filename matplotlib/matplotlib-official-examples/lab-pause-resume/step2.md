# Define the Animation

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
