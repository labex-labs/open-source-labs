# データの整形

時々、データが最初から scikit-learn に必要な形状になっていない場合があります。そのような場合、データを前処理して `(n_samples, n_features)` の形状に変換する必要があります。データを整形する例として、1797個の8x8の手書き数字の画像からなる digits データセットがあります。

```python
digits = datasets.load_digits()
print(digits.images.shape)
```

出力:

```
(1797, 8, 8)
```

このデータセットを scikit-learn で使用するには、各8x8の画像を長さ64の特徴量ベクトルに整形する必要があります。

```python
data = digits.images.reshape((digits.images.shape[0], -1))
```
