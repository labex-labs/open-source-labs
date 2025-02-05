# Create a random matrix

Next, we will create a random matrix using numpy. We will use the `rand` method to create a 5x3 matrix with random values between 0 and 1. We will also set a random seed to ensure reproducibility of the results.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

X = 10*np.random.rand(5, 3)
```
