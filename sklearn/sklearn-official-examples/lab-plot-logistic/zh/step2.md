# 生成一个简单的数据集

下一步是生成一个简单的数据集，它是一条带有一些高斯噪声的直线。我们将使用 `numpy` 来生成这个数据集。

```python
# 生成一个简单的数据集，它只是一条带有一些高斯噪声的直线：
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(float)
X[X > 0] *= 4
X += 0.3 * np.random.normal(size=n_samples)

X = X[:, np.newaxis]
```
