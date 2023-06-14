# Create the Animation

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

#
