# データを準備する

Irisデータセットの最初の2つの特徴量、つまり花弁の長さと花弁の幅のみを取り出します。その後、データを特徴行列`X`とターゲットベクトル`y`に分割します。

```python
X = iris.data[:, :2]
y = iris.target
```
