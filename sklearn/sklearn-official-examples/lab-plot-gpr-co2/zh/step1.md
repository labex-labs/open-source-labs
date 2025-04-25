# 构建数据集

第一步是通过从收集空气样本的莫纳罗亚天文台获取数据来构建数据集。我们感兴趣的是估计二氧化碳浓度并将其外推到未来几年。我们加载 OpenML 中可用的原始数据集，并通过计算每月平均值和删除未收集测量值的月份来预处理数据集。

```python
from sklearn.datasets import fetch_openml
import pandas as pd

co2 = fetch_openml(data_id=41187, as_frame=True, parser="pandas")
co2_data = co2.frame
co2_data["date"] = pd.to_datetime(co2_data[["year", "month", "day"]])
co2_data = co2_data[["date", "co2"]].set_index("date")
co2_data = co2_data.resample("M").mean().dropna(axis="index", how="any")

X = (co2_data.index.year + co2_data.index.month / 12).to_numpy().reshape(-1, 1)
y = co2_data["co2"].to_numpy()
```
