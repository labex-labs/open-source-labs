# Define the Curve

Next, we define the curve that we want to draw the error band around. In this example, we will be using a parametrized curve. A parametrized curve x(t), y(t) can directly be drawn using `~.Axes.plot`.

```python
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)
```
