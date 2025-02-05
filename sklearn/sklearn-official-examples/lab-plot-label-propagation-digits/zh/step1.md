# 加载并打乱数据

我们首先加载数字数据集并随机打乱数据。

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```
