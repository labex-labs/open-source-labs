# 定义分布

我们定义了一个包含不同缩放器、转换器和归一化器的列表，以便将数据缩放到预定义范围内，并将它们存储在一个名为 `distributions` 的列表中。

```python
# 定义分布
distributions = [
    ("未缩放的数据", X),
    ("标准缩放后的数据", StandardScaler().fit_transform(X)),
    ("最小-最大缩放后的数据", MinMaxScaler().fit_transform(X)),
    ("稳健缩放后的数据", RobustScaler(quantile_range=(25, 75)).fit_transform(X)),
    ("样本-wise L2 归一化后的数据", Normalizer().fit_transform(X)),
    ("分位数变换后的数据（均匀概率密度函数）", QuantileTransformer(output_distribution="uniform").fit_transform(X)),
    ("分位数变换后的数据（高斯概率密度函数）", QuantileTransformer(output_distribution="normal").fit_transform(X)),
    ("幂变换后的数据（Yeo-Johnson 方法）", PowerTransformer(method="yeo-johnson").fit_transform(X)),
    ("幂变换后的数据（Box-Cox 方法）", PowerTransformer(method="box-cox").fit_transform(X)),
]
```
