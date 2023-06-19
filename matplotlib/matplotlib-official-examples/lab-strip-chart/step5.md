# Set up the Plot

We create a new figure and axis object and initialize the Scope class. We then pass the update and emitter functions to the FuncAnimation method to create the animation.

```python
fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)

plt.show()
```
