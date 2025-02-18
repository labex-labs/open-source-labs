# データを作成する

この例では、`numpy.random.randn()` を使用してランダムなデータセットを作成します。

```python
np.random.seed(19680801)
x = 30*np.random.randn(10000)
mu = x.mean()
median = np.median(x)
sigma = x.std()
```
