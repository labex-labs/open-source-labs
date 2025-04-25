# データセットを作成する

最初のステップは、空気サンプルを収集したモナロア天文台からデータセットを作成することです。私たちは、CO2 の濃度を推定し、さらに数年間外挿することに興味があります。OpenML にある元のデータセットを読み込み、月平均をとり、測定が行われていない月を除外することでデータセットを前処理します。

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
