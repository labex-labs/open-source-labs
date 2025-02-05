# Creating the Animation

The final step is to create the animation. We do this using the FuncAnimation function from the animation module. This function takes a few arguments, including the figure object, the function that will update the plot, and the number of frames to use.

```python
def animate(i):
    scat.set_offsets((x[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=50)
```
