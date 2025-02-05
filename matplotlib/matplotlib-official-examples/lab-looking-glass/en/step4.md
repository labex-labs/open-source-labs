# Plotting the Data

We will plot the random data generated in Step 2 using the `plot()` function twice. The first plot will have an alpha value of 0.2 and the second plot will have an alpha value of 1.0 and a clip path set to the yellow circle patch.

```python
ax.plot(x, y, alpha=0.2)
line, = ax.plot(x, y, alpha=1.0, clip_path=circ)
ax.set_title("Left click and drag to move looking glass")
```
