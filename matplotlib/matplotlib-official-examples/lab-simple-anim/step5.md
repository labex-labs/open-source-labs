# Create the Animation Object

Now we can create the animation object using the `FuncAnimation()` function. We will pass in the figure object, the animation function, the update interval, and the number of frames to be saved.

```python
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
```
