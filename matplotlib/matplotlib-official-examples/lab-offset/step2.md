# Create Data

Next, we create the data that we will use in our plot. In this example, we will be using NumPy to generate the data.

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
```
