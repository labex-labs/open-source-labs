# Create the Animation

Finally, we will create the animation using the FuncAnimation object, passing in the figure, the update function, the interval between frames in milliseconds, and the number of frames to save.

```python
animation = FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```
