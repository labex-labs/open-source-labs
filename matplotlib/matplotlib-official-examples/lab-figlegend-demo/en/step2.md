# Creating a Basic Plot

To create a basic plot, we need to define the x and y values and then plot them using `plt.plot()`. Here, we will plot two sine waves.

```python
x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.sin(4 * np.pi * x)

plt.plot(x, y1, label='sin(2pix)')
plt.plot(x, y2, label='sin(4pix)')
```
