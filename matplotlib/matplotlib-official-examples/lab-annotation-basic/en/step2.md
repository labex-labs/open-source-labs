# Create a Plot

Next, we will create a plot using Matplotlib. In this example, we will plot the cosine function over a range of values.

```python
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
```
