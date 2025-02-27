# データをシャッフルする

分析におけるランダム性を保証するため、データセット内のサンプルの順序をシャッフルしましょう。

```python
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]
```
