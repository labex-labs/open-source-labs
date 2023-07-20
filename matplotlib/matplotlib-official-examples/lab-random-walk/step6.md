# Create Animation

We create an animation using the `FuncAnimation` class from `matplotlib.animation`. We pass the figure object, the update function, the total number of frames (which is equal to the number of steps in the random walks), the list of all random walks, and the list of all lines as arguments to the `FuncAnimation` constructor.

```python
# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
```
