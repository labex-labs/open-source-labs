# 逆変換

ランダム射影変換器には、射影行列の逆行列を計算するオプションがあります。射影されたデータに逆変換を適用することで、この機能を調べてみましょう。

```python
transformer = random_projection.SparseRandomProjection(compute_inverse_components=True)
X_new = transformer.fit_transform(X)

# Compute the inverse transform
X_new_inversed = transformer.inverse_transform(X_new)
```

このステップでは、`compute_inverse_components` パラメータを `True` に設定して `SparseRandomProjection` クラスのインスタンスを作成します。その後、変換器をデータ `X` に適合させて変換を適用します。最後に、射影されたデータ `X_new` に対して `inverse_transform` メソッドを呼び出すことで逆変換を計算します。
