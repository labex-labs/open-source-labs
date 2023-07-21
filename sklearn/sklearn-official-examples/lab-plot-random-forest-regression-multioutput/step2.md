# Create a Random Dataset

Next, we will create a random dataset to use for our regression. We will use `numpy` to create a set of 600 x-values between -100 and 100, and corresponding y-values calculated from the sine and cosine of the x-values plus some random noise.

```python
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(600, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y += 0.5 - rng.rand(*y.shape)
```
