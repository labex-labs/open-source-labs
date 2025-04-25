# データの作成

この実験用にランダムなデータセットを生成します。データセットには、3 つの変数 `x`、`y`、および `z` があります。`x` と `y` を平均 0、標準偏差 0.5 の正規分布に従うランダムな変数として定義します。`z` も平均 0、標準偏差 0.1 の正規分布に従います。

```python
e = np.exp(1)
np.random.seed(4)

y = np.random.normal(scale=0.5, size=(30000))
x = np.random.normal(scale=0.5, size=(30000))
z = np.random.normal(scale=0.1, size=len(x))
```
