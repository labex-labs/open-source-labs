# CCA

#### CCA モデルをフィットさせる

`CCA` アルゴリズムは PLS の特殊なケースで、標準相関分析（Canonical Correlation Analysis）を表します。これは 2 つの変数セット間の相関を見つけます。

```python
cca = CCA(n_components=2)
cca.fit(X, Y)
```

#### データを変換する

フィットさせたモデルを使って元のデータを変換することができます。変換後のデータは次元が削減されています。

```python
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
```
