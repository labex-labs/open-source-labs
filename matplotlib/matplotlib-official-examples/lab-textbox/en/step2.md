# Create the Initial Plot

Next, we create the initial plot that will be updated based on the user's input. In this example, we create a plot of a function with `t` as the independent variable.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-2.0, 2.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)
```
