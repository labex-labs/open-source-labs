# データの生成

`numpy.random.standard_normal()` と `numpy.random.standard_normal()` を使って 100,000 個のデータポイントを生成します。`standard_normal()` は平均 0、標準偏差 1 の標準正規分布から乱数を生成します。

```python
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()
```
