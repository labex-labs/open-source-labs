# 乱数シードを設定してデータを生成する

このステップでは、乱数シードを設定してデータを生成します。平均200、標準偏差25の正規分布から100個のデータポイントを生成します。

```python
np.random.seed(19680801)
mu = 200
sigma = 25
data = np.random.normal(mu, sigma, size=100)
```
