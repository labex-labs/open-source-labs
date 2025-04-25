# データセットを読み込む

`datasets.load_digits(return_X_y=True)` を使用して、数字のデータセットを読み込みます。また、`StandardScaler().fit_transform(X)` を使用してデータを標準化します。目的変数は 2 値になり、0-4 は 0 として分類され、5-9 は 1 として分類されます。

```python
X, y = datasets.load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X)
y = (y > 4).astype(int)
```
