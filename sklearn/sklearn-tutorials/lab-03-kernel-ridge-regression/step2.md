# Generate Synthetic Data

Next, let's generate some synthetic data to work with. We will create a sinusoidal target function and add some random noise to it.

```python
# Generate input data
np.random.seed(0)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel()
y += 0.5 * (0.5 - np.random.rand(y.size))
```
