# 生成玩具数据

我们现在将使用 scikit-learn 中的 make_regression 函数生成一个玩具数据集。我们将生成一个包含 20 个样本、一个特征且随机种子为 0 的数据集。我们还将向数据集中添加一些噪声。

```python
rng = np.random.RandomState(0)
X, y = make_regression(
    n_samples=20, n_features=1, random_state=0, noise=4.0, bias=100.0
)
```
