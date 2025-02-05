# Create the Plot

Now, we can create our plot. We will generate some data using NumPy and plot a damped exponential decay curve.

```python
x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

plt.plot(x, y, 'k')
```
