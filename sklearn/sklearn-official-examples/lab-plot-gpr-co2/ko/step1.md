# 데이터셋 구축

첫 번째 단계는 마우나 로아 천문대에서 수집한 공기 샘플로부터 데이터셋을 구축하는 것입니다. 우리는 CO2 농도를 추정하고 향후 연도에 대해 외삽하는 데 관심이 있습니다. OpenML 에서 사용 가능한 원본 데이터셋을 로드하고, 월 평균을 계산하고 측정값이 수집되지 않은 달을 제거하여 데이터셋을 전처리합니다.

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
