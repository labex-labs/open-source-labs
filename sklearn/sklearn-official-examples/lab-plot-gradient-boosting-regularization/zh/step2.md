# 加载并分割数据

我们将使用 make_hastie_10_2 数据集，并将其分割为训练集和测试集。

```python
X, y = datasets.make_hastie_10_2(n_samples=4000, random_state=1)

# map labels from {-1, 1} to {0, 1}
labels, y = np.unique(y, return_inverse=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)
```
