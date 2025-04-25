# 生成数据

我们将为本次实验生成一个简单的数据集。我们将生成 500 个训练样本和 20 个测试样本。我们还将生成 20 个异常样本。

```python
random_state = 42
rng = np.random.RandomState(random_state)

# 生成训练数据
X = 0.3 * rng.randn(500, 2)
X_train = np.r_[X + 2, X - 2]
# 生成一些常规的新观测值
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
# 生成一些异常的新观测值
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
```
