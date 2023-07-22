# Create data for the plot

Create some data for the plot. In this example, we will create `x` and `y` arrays using the `numpy` library.

```python
x = np.linspace(-3, 3, 201)
y = np.tanh(x) + 0.1 * np.cos(5 * x)
```
