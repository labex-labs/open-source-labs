# Create the Animation

We will now create the animation using the ArtistAnimation method. We will be passing in the figure object, the ims list, the interval between frames, and the repeat delay.

```python
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
```
