# PLSRegression

#### PLSRegression モデルをフィットさせる

正則化線形回帰の一種である `PLSRegression` アルゴリズムから始めます。このモデルをデータにフィットさせます。

```python
pls = PLSRegression(n_components=2)
pls.fit(X, Y)
```

#### データを変換する

フィットさせたモデルを使って元のデータを変換することができます。変換後のデータは次元が削減されています。

```python
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)
```
