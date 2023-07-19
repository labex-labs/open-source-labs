# Plot the Sine Wave

We create a sine wave using numpy and plot it on the Matplotlib figure. We also label the x and y axes.

```python
t = np.arange(0, 3, .01)
line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
ax.set_xlabel("time [s]")
ax.set_ylabel("f(t)")
```
