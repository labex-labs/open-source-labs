# Create a Random Dataset

In this step, we will create a random dataset. We will use the `numpy` library to create a sorted array of 100 elements, with random values from 0 to 200, then subtract 100 from each element. Then we will use `numpy` to compute the sine and cosine of each element, and join these arrays together into a 2D array of shape (100, 2) to create the `y` array. We will also add random noise to every fifth element.

```python
# Create a random dataset
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(100, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y[::5, :] += 0.5 - rng.rand(20, 2)
```
