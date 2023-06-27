# Create Data

We will create a dataset of 20 points, where the first 10 points belong to class 1 and the last 10 points belong to class -1.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
```
