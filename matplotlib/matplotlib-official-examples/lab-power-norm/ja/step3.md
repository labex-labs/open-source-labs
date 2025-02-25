# データの作成

このステップでは、`multivariate_normal()` を使ってデータを作成する必要があります。この関数は、多変量正規分布からの乱数サンプルを生成します。

```python
data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000)
])
```
