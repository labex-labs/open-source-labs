# データセットに強いアウトライアーを追加する

データセットに4つの強いアウトライアーを追加します。これらのアウトライアーについては、正規分布を使って乱数値を生成します。その後、これらのアウトライアーをデータセットに追加します。

```python
X_outliers = rng.normal(0, 0.5, size=(4, 1))
y_outliers = rng.normal(0, 2.0, size=4)
X_outliers[:2, :] += X.max() + X.mean() / 4.0
X_outliers[2:, :] += X.min() - X.mean() / 4.0
y_outliers[:2] += y.min() - y.mean() / 4.0
y_outliers[2:] += y.max() + y.mean() / 4.0
X = np.vstack((X, X_outliers))
y = np.concatenate((y, y_outliers))
```
