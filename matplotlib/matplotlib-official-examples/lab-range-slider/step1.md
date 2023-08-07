# Generate a fake image

First, we will generate a fake grayscale image using NumPy's random module. We will set the seed to ensure that the results are reproducible.

```python
np.random.seed(19680801)
N = 128
img = np.random.randn(N, N)
```
