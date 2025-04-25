# データセットの読み込み

Scikit-Learn からカリフォルニア住宅データセットを読み込みます。計算時間を短縮するため、2,000 サンプルのみを使用します。

```python
N_SPLITS = 5

rng = np.random.RandomState(0)

X_full, y_full = fetch_california_housing(return_X_y=True)
X_full = X_full[::10]
y_full = y_full[::10]
n_samples, n_features = X_full.shape
```
