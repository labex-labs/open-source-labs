# データを生成する

例で使用するために、いくつかのランダムなデータを生成します。NumPy の関数 `random.lognormal()` を使って、平均が 1.5、標準偏差が 1.75 の対数正規分布のデータを生成します。4 つの変数の 37 個のサンプルを生成し、`data` 変数に格納します。また、各変数に対するラベルのリストも作成します。

```python
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
