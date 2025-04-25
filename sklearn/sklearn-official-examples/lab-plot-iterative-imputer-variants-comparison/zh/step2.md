# 加载数据集

我们将从 Scikit-Learn 中加载加利福尼亚住房数据集。为了减少计算时间，我们只使用 2k 个样本。

```python
N_SPLITS = 5

rng = np.random.RandomState(0)

X_full, y_full = fetch_california_housing(return_X_y=True)
X_full = X_full[::10]
y_full = y_full[::10]
n_samples, n_features = X_full.shape
```
