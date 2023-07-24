# Create the Animation

We will now create the animation using the FuncAnimation function from Matplotlib.

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```
