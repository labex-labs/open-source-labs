# 创建数据集

我们将创建一个包含 3 个特征的数据集，其中第一个特征与目标具有线性关系，第二个特征与目标具有非线性关系，第三个特征则完全不相关。我们将为这个数据集创建 1000 个样本。

```python
np.random.seed(0)
X = np.random.rand(1000, 3)
y = X[:, 0] + np.sin(6 * np.pi * X[:, 1]) + 0.1 * np.random.randn(1000)
```
