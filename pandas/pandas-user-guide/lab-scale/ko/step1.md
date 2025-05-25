# 데이터 세트 생성

첫 번째 단계는 테스트를 위해 대규모 데이터 세트를 생성하는 것입니다. parquet 파일에 저장할 수 있는 많은 열을 가진 데이터 세트를 생성합니다. 이 단계에는 pandas 및 numpy 라이브러리가 필요합니다.

```python
import pandas as pd
import numpy as np

def make_timeseries(start="2000-01-01", end="2000-12-31", freq="1D", seed=None):
    # Function to generate timeseries data
    index = pd.date_range(start=start, end=end, freq=freq, name="timestamp")
    n = len(index)
    state = np.random.RandomState(seed)
    columns = {
        "name": state.choice(["Alice", "Bob", "Charlie"], size=n),
        "id": state.poisson(1000, size=n),
        "x": state.rand(n) * 2 - 1,
        "y": state.rand(n) * 2 - 1,
    }
    df = pd.DataFrame(columns, index=index, columns=sorted(columns))
    if df.index[-1] == end:
        df = df.iloc[:-1]
    return df

timeseries = [
    make_timeseries(freq="1T", seed=i).rename(columns=lambda x: f"{x}_{i}")
    for i in range(10)
]
ts_wide = pd.concat(timeseries, axis=1)
ts_wide.to_parquet("timeseries_wide.parquet")
```
