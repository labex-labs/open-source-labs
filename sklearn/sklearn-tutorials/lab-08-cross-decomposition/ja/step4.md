# PLSCanonical

#### PLSCanonical モデルをフィットさせる

次に、2つの行列間の標準相関を見つける `PLSCanonical` アルゴリズムを使用します。このアルゴリズムは、特徴量間に多重共線性がある場合に役立ちます。

```python
plsc = PLSCanonical(n_components=2)
plsc.fit(X, Y)
```

#### データを変換する

フィットさせたモデルを使って元のデータを変換することができます。変換後のデータは次元が削減されています。

```python
X_transformed = plsc.transform(X)
Y_transformed = plsc.transform(Y)
```
