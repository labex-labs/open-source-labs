# 変換されたデータセット

組み合わせた特徴を使ってデータセットを変換します。

```python
X_features = combined_features.fit(X, y).transform(X)
print("Combined space has", X_features.shape[1], "features")
```
