# 生成玩具数据

我们现在将使用scikit-learn中的make_regression函数生成一个玩具数据集。我们将生成一个包含20个样本、一个特征且随机种子为0的数据集。我们还将向数据集中添加一些噪声。

```python
rng = np.random.RandomState(0)
X, y = make_regression(
    n_samples=20, n_features=1, random_state=0, noise=4.0, bias=100.0
)
```
