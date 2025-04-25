# 特徴量の数を一定に保つ

デフォルトでは、scikit-learn の欠損値補完ツールは欠損値のみの列を削除します。ただし、場合によっては、データの形状を維持するために空の特徴量を残す必要があります。これは、`keep_empty_features`パラメータを True に設定することで達成できます。

```python
imputer = SimpleImputer(keep_empty_features=True)
X = np.array([[np.nan, 1], [np.nan, 2], [np.nan, 3]])
imputed_X = imputer.fit_transform(X)
```
