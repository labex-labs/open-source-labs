# PLSSVD

#### PLSSVD モデルをフィットさせる

`PLSSVD` アルゴリズムは、交差共分散行列の特異値分解（Singular Value Decomposition: SVD）をただ一度だけ計算する `PLSCanonical` の簡略化バージョンです。このアルゴリズムは、成分数が 1 に制限されている場合に役立ちます。

```python
plssvd = PLSSVD(n_components=1)
plssvd.fit(X, Y)
```

#### データを変換する

フィットさせたモデルを使って元のデータを変換することができます。変換後のデータは次元が削減されています。

```python
X_transformed = plssvd.transform(X)
Y_transformed = plssvd.transform(Y)
```
