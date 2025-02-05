# 加载并预处理艾姆斯房屋数据

我们加载艾姆斯房屋数据集，并通过仅保留数值列以及移除包含缺失值（NaN）或无穷大值（Inf）的列来对其进行预处理。要预测的目标是每栋房屋的售价。

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import quantile_transform

ames = fetch_openml(name="house_prices", as_frame=True, parser="pandas")

# 仅保留数值列
X = ames.data.select_dtypes(np.number)

# 移除包含缺失值（NaN）或无穷大值（Inf）的列
X = X.drop(columns=["LotFrontage", "GarageYrBlt", "MasVnrArea"])

# 让价格以千美元为单位
y = ames.target / 1000
y_trans = quantile_transform(
    y.to_frame(), n_quantiles=900, output_distribution="normal", copy=True
).squeeze()
```
