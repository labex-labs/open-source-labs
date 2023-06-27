# Generate Data

We generate 40 separable points using numpy's `random.randn` function. The first 20 points have a mean of [-2, -2] and the next 20 points have a mean of [2, 2]. We then assign a class label of 0 to the first 20 points and a class label of 1 to the next 20 points.

```python
np.random.seed(0)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20
```
