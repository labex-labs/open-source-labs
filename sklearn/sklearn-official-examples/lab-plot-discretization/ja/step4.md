# 入力特徴量を離散化する

このステップでは、入力特徴量を離散化するために KBinsDiscretizer クラスを使います。10 個のビンを作成し、ワンホットエンコーディングを使ってデータを変換します。

```python
enc = KBinsDiscretizer(n_bins=10, encode="onehot")
X_binned = enc.fit_transform(X)
```
