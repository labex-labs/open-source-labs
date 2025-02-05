# Create the animation

Finally, we can create the animation using the `FuncAnimation` class. We will pass the `fig`, `run`, `data_gen`, `init_func`, and `interval` parameters to create the animation. We will also set the `save_count` parameter to 100 to ensure that only the last 100 frames are saved.

```python
ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init,
                              save_count=100)
```
