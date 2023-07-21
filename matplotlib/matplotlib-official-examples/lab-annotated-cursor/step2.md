# Create a plot

We create a simple plot of a parabola using NumPy's `linspace` function to generate 1000 values between -5 and 5 for x, and then compute y as the square of x.

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x**2

line, = ax.plot(x, y)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
```
