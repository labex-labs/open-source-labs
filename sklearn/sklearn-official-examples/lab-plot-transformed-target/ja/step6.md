# エイムズ住宅データを読み込んで前処理する

エイムズ住宅データセットを読み込み、数値列のみを残し、NaN または Inf 値を持つ列を削除することで前処理します。予測対象のターゲットは、各住宅の販売価格です。

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import quantile_transform

ames = fetch_openml(name="house_prices", as_frame=True, parser="pandas")

# 数値列のみを残す
X = ames.data.select_dtypes(np.number)

# NaN または Inf 値を持つ列を削除する
X = X.drop(columns=["LotFrontage", "GarageYrBlt", "MasVnrArea"])

# 価格を千ドル単位にする
y = ames.target / 1000
y_trans = quantile_transform(
    y.to_frame(), n_quantiles=900, output_distribution="normal", copy=True
).squeeze()
```
