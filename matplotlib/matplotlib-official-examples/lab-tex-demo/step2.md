# Create a Simple Line Plot

In this step, we will create a simple line plot using Matplotlib. We will start by generating some data to plot using the NumPy `linspace()` function and the `cos()` function. Then, we will use the `plot()` function to create the plot.

```python
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.show()
```
