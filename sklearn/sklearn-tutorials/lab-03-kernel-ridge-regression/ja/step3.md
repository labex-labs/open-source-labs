# Kernel Ridge Regression モデルの適合

次に、データに Kernel Ridge Regression モデルを適合させましょう。非線形回帰に一般的に使用される RBF（Radial Basis Function）カーネルを使用します。

```python
# Fit Kernel Ridge Regression model
alpha = 1.0  # 正則化パラメータ
gamma = 0.1  # RBF カーネルのカーネル係数
krr = KernelRidge(alpha=alpha, kernel='rbf', gamma=gamma)
krr.fit(X, y)
```
