# Set up the plot

Now, we need to set up the plot. We will create a figure and an axes object using Matplotlib's `subplots()` function. We will also create a line object to represent the sine wave.

```python
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
```
