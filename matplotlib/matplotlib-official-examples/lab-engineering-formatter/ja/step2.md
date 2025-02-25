# 人工データを作成する

描画するためにいくつかの人工データを作成する必要があります。この実験では、周波数（Hz）の対数に対して電力（ワット）の対数をプロットします。データの生成には `numpy` ライブラリを使用します。

```python
# Fixing random state for reproducibility
prng = np.random.RandomState(19680801)

# Create artificial data to plot.
# The x data span over several decades to demonstrate several SI prefixes.
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2
```
