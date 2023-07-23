# Generate Data

We will generate some data for training, testing, and outliers using numpy. We will generate 100 normal training observations, 20 normal testing observations, and 20 abnormal novel observations.

```python
np.random.seed(42)

xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
