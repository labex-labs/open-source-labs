# ランダムなデータを生成する

NumPyの`random.normal`関数を使って、2セットのランダムなデータを生成します。これらのセットは、異なるスタイルのヒストグラムを作成するために使用されます。

```python
np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)
```
