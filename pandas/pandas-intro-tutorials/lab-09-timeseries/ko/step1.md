# 필요한 라이브러리 가져오기 및 데이터 로드

먼저, 필요한 Python 라이브러리를 가져오고 대기 질 데이터를 로드해야 합니다. 데이터는 2 차원 레이블이 지정된 데이터 구조인 pandas DataFrame 으로 읽혀집니다.

```python
# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load the air quality data
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# rename the "date.utc" column to "datetime"
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```
