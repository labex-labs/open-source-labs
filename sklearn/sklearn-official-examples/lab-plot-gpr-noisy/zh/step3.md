# 添加噪声

在这一步中，我们将向生成的数据中添加一些噪声，以创建一个更现实的训练数据集。

```python
rng = np.random.RandomState(0)
X_train = rng.uniform(0, 5, size=20).reshape(-1, 1)
y_train = target_generator(X_train, add_noise=True)
```
