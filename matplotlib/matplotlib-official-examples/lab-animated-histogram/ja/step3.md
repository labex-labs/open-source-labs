# データとヒストグラムの作成

NumPy を使ってデータとヒストグラムを作成します。

```python
# histogram our data with numpy
data = np.random.randn(1000)
n, _, _ = plt.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
```
