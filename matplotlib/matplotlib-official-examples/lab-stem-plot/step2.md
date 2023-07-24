# Generate Data

Next, we need to generate some data to use in our stem plot. We will create two arrays using the Numpy library.

```python
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
```
