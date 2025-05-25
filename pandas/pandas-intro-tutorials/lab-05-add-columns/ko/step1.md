# Pandas 임포트 및 데이터 로드

먼저, pandas 라이브러리를 임포트하고 CSV 파일에서 대기 질 데이터를 로드합니다.

```python
# Import pandas library
import pandas as pd

# Load air quality data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
```
